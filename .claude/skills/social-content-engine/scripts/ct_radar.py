#!/usr/bin/env python3
"""Read-only, bounded Crypto Twitter X API collector + offline topic ranking.

No browser automation, session cookies, passwords, account writes, or dependencies.
The report is a set of discussion signals, NOT independently verified news.
"""
from __future__ import annotations

import argparse
import datetime as dt
import json
import math
import os
import re
import sys
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

API = "https://api.x.com/2/tweets/search/recent"
UTC = dt.timezone.utc


def now_utc():
    return dt.datetime.now(UTC)


def iso(t):
    return t.astimezone(UTC).strftime("%Y-%m-%dT%H:%M:%SZ")


def parse_time(v):
    if not v:
        return None
    try:
        return dt.datetime.fromisoformat(v.replace("Z", "+00:00")).astimezone(UTC)
    except (ValueError, TypeError):
        return None


def load_json(path):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def save_json(path, data):
    dest = Path(path)
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def safe_post(raw, users=None):
    """Normalize X API or user-provided records without inventing metrics/author handles."""
    uid = str(raw.get("author_id") or "")
    user = (users or {}).get(uid, {})
    p_id = str(raw.get("id") or raw.get("post_id") or "")
    if not re.fullmatch(r"[0-9]{5,30}", p_id):
        return None
    ts = parse_time(raw.get("created_at"))
    if not ts:
        return None
    metric = raw.get("public_metrics") or raw.get("metrics") or {}
    m = {k: max(0, int(metric.get(k, 0))) if str(metric.get(k, 0)).isdigit() else 0
         for k in ("like_count", "retweet_count", "reply_count", "quote_count")}
    if not raw.get("public_metrics") and raw.get("metrics"):
        for old, new in (("likes", "like_count"), ("reposts", "retweet_count"),
                         ("replies", "reply_count"), ("quotes", "quote_count")):
            if old in metric:
                v = metric[old]
                m[new] = max(0, int(v)) if str(v).isdigit() else 0
    username = raw.get("username") or raw.get("author_handle") or user.get("username") or None
    if username:
        username = str(username).lstrip("@")
        if not re.fullmatch(r"[A-Za-z0-9_]{1,15}", username):
            username = None
    url = "https://x.com/i/web/status/" + p_id
    return {"id": p_id, "created_at": iso(ts), "url": url,
            "author_handle": username, "author_id": uid or None,
            "text": str(raw.get("text") or "")[:1200], "lang": raw.get("lang"),
            "metrics": m, "topics": list(raw.get("topics", []))}


def collect(args):
    token = os.getenv("X_API_BEARER_TOKEN", "").strip()
    if not token:
        raise RuntimeError("X_API_BEARER_TOKEN is not configured. No API requests were made. See docs/SETUP_EN.md.")
    cfg = load_json(args.topics)
    topics = cfg.get("topics", [])
    if not isinstance(topics, list) or not 1 <= len(topics) <= 20:
        raise ValueError("topics.json needs 1-20 named topic entries")
    if not 1 <= args.max_queries <= 20 or not 10 <= args.per_topic <= 100 or not 1 <= args.hours <= 168:
        raise ValueError("max-queries=1..20; per-topic=10..100; hours=1..168")
    if not 1 <= args.timeout <= 60:
        raise ValueError("timeout must be 1..60 seconds")
    begin = now_utc() - dt.timedelta(hours=args.hours)
    all_posts = {}
    stats = []
    for item in topics[:args.max_queries]:
        name, query = item.get("name"), item.get("query")
        if not isinstance(name, str) or not name.strip() or not isinstance(query, str) or not query.strip():
            raise ValueError("Each topic requires name and query")
        params = urllib.parse.urlencode({
            "query": query, "max_results": str(args.per_topic),
            "start_time": iso(begin),
            "tweet.fields": "created_at,author_id,public_metrics,lang",
            "expansions": "author_id", "user.fields": "username",
        })
        request = urllib.request.Request(API + "?" + params,
                                         headers={"Authorization": "Bearer " + token,
                                                  "User-Agent": "SocialContentEngineCTRadar/1.0"},
                                         method="GET")
        try:
            with urllib.request.urlopen(request, timeout=args.timeout) as resp:
                obj = json.load(resp)
        except urllib.error.HTTPError as err:
            # Intentionally do not echo headers, response body, or credentials.
            raise RuntimeError(f"X API returned HTTP {err.code} for topic '{name}'. "
                               "Check authorization, credits, and rate limits; no browser fallback.") from None
        except urllib.error.URLError:
            raise RuntimeError(f"X API network error for '{name}'. No results fabricated.") from None
        users = {str(u.get("id")): u for u in obj.get("includes", {}).get("users", [])}
        count = 0
        for raw in obj.get("data") or []:
            post = safe_post(raw, users)
            if not post:
                continue
            count += 1
            old = all_posts.get(post["id"])
            if old:
                if name not in old["topics"]:
                    old["topics"].append(name)
            else:
                post["topics"] = [name]
                all_posts[post["id"]] = post
        stats.append({"topic": name, "posts_returned": count})
    save_json(args.output, {
        "status": "OK", "source": "x-api-recent-search", "collected_at": iso(now_utc()),
        "window_hours": args.hours, "request_count": len(stats),
        "notice": "X discussion signals only. Stories and factual claims are not independently verified.",
        "queries": stats, "posts": list(all_posts.values())
    })
    print(f"Collected {len(all_posts)} unique public X posts via {len(stats)} X API searches; saved {args.output}")


def tokens(text):
    norm = re.sub(r"https?://\S+", "", text.lower())
    return set(re.findall(r"[a-z0-9]{3,}|[\u4e00-\u9fff]{2,}", norm))


def near_same(x, y):
    if x["id"] == y["id"]:
        return True
    a, b = re.sub(r"\s+", "", x["text"].lower())[:70], re.sub(r"\s+", "", y["text"].lower())[:70]
    if len(a) > 30 and (a in b or b in a):
        return True
    ta, tb = tokens(x["text"]), tokens(y["text"])
    return bool(ta and tb and len(ta & tb) / len(ta | tb) >= 0.82)


def score(post, now):
    ts = parse_time(post["created_at"])
    age = max(0.05, (now - ts).total_seconds() / 3600)
    m = post["metrics"]
    engagement = m["like_count"] + 2.4 * m["retweet_count"] + 1.3 * m["reply_count"] + 1.8 * m["quote_count"]
    # Bounded heuristic. Engagement is neither truth nor a verified measure of CT-wide popularity.
    return round(0.58 * math.log1p(engagement) + 0.22 * math.log1p(engagement / (age + 1))
                 + 1.8 * math.exp(-age / 18) + 0.3 * len(post.get("topics", [])), 4)


def analyze(args):
    data = load_json(args.input)
    raw = data.get("posts", []) if isinstance(data, dict) else data
    if not isinstance(raw, list):
        raise ValueError("Input must be a list or an object with a posts list")
    now = parse_time(args.now) if args.now else now_utc()
    if not now:
        raise ValueError("Invalid --now timestamp")
    valid = []
    for item in raw:
        p = safe_post(item)
        if p:
            # Preserve already normalised records: safe_post accepts public_metrics/metrics.
            p["topics"] = [str(t) for t in item.get("topics", []) if isinstance(t, str)]
            age = (now - parse_time(p["created_at"])).total_seconds() / 3600
            if 0 <= age <= args.hours:
                p["score"] = score(p, now)
                valid.append(p)
    valid.sort(key=lambda p: (-p["score"], p["id"]))
    selected, topic_counts = [], {}
    for p in valid:
        if any(near_same(p, q) for q in selected):
            continue
        category = p["topics"][0] if p["topics"] else "Other"
        if topic_counts.get(category, 0) >= args.per_topic:
            continue
        selected.append(p)
        topic_counts[category] = topic_counts.get(category, 0) + 1
        if len(selected) >= args.limit:
            break
    report = {"generated_at": iso(now), "source": data.get("source", "user-provided") if isinstance(data, dict) else "user-provided",
              "source_posts": len(raw), "eligible_posts": len(valid), "selected": selected,
              "notice": "Heuristic X discussion signals, not official trends or verified news. Verify important claims before drafting."}
    save_json(args.output, report)
    lines = ["# Daily Crypto Twitter Radar", "", f"Generated (UTC): {iso(now)}  ",
             f"Source: {report['source']}  ", f"Eligible records: {len(valid)}; selected signals: {len(selected)}", "",
             "**Method:** Read-only X discussion sampling, engagement/freshness heuristic and topic diversity. "
             "Not an exhaustive CT ranking. X posts are not proof of the claims they contain.", ""]
    if not selected:
        lines.append("No verified-in-window source posts available. No topics fabricated. Check the API/source and window.")
    for i, p in enumerate(selected, 1):
        topic = p["topics"][0] if p["topics"] else "Uncategorised"
        excerpt = p["text"].replace("\n", " ")[:240].replace("|", "/")
        m = p["metrics"]
        lines += [f"## {i}. {topic} — discussion signal", "",
                  f"- Original post: {p['url']}",
                  f"- Author: {'@' + p['author_handle'] if p['author_handle'] else 'UNKNOWN'}",
                  f"- Posted (UTC): {p['created_at']}",
                  f"- Engagement at collection: likes {m['like_count']}, reposts {m['retweet_count']}, replies {m['reply_count']}, quotes {m['quote_count']}",
                  f"- Excerpt (not independently verified): {excerpt}",
                  "- Follow-up: check the event and any source-linked evidence; look for independent reporting and counterarguments.",
                  "- Writing opportunity: explain the mechanism, challenge the assumption, or connect it to your OWN stated view (not a fabricated opinion).", ""]
    dest = Path(args.markdown)
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"Selected {len(selected)} discussion signals; saved {args.output} and {args.markdown}")


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="command", required=True)
    c = sub.add_parser("collect", help="Read-only X API recent search with a bearer token")
    c.add_argument("--topics", default="examples/topics.example.json")
    c.add_argument("--output", default="data/private/ct-posts.json")
    c.add_argument("--hours", type=int, default=24)
    c.add_argument("--max-queries", type=int, default=6)
    c.add_argument("--per-topic", type=int, default=10)
    c.add_argument("--timeout", type=int, default=20)
    c.set_defaults(func=collect)
    a = sub.add_parser("rank", help="Rank supplied/X API JSON; no network access")
    a.add_argument("--input", required=True)
    a.add_argument("--output", default="reports/private/radar.json")
    a.add_argument("--markdown", default="reports/private/radar.md")
    a.add_argument("--limit", type=int, default=6)
    a.add_argument("--per-topic", type=int, default=2)
    a.add_argument("--hours", type=int, default=36)
    a.add_argument("--now", help="Optional ISO UTC time for repeatable tests")
    a.set_defaults(func=analyze)
    args = parser.parse_args(argv)
    if args.command == "rank" and (not 1 <= args.limit <= 20 or not 1 <= args.per_topic <= 10 or not 1 <= args.hours <= 168):
        parser.error("limit=1..20, per-topic=1..10, hours=1..168")
    try:
        args.func(args)
    except (RuntimeError, ValueError, OSError, json.JSONDecodeError) as err:
        print("ERROR: " + str(err), file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
