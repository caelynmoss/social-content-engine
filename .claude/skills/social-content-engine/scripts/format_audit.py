#!/usr/bin/env python3
"""Private, offline, per-account comparison of X formats. Never contacts X or uploads data."""
import argparse
import csv
import json
import statistics
import sys
from collections import defaultdict
from pathlib import Path

FORMATS = {"ARTICLE", "LONG_POST", "SHORT_POST", "THREAD", "OTHER"}
VALID_METRICS = ("views", "engagements", "saves")

def summarize(csv_path, account_id, metric="views", category="", min_n=5):
    if metric not in VALID_METRICS:
        raise ValueError("Unsupported metric")
    buckets = defaultdict(list)
    rejected = 0
    with open(csv_path, encoding="utf-8-sig", newline="") as f:
        reader = csv.DictReader(f)
        required = {"account_id", "format", "category", "is_original", metric}
        if not required.issubset(reader.fieldnames or []):
            raise ValueError("CSV must include: " + ", ".join(sorted(required)))
        for row in reader:
            if row.get("account_id", "").strip() != account_id:
                continue
            if category and row.get("category", "").strip() != category:
                continue
            if row.get("is_original", "").strip().lower() not in ("true", "1", "yes"):
                continue
            fmt = row.get("format", "").strip().upper()
            if fmt not in FORMATS:
                rejected += 1
                continue
            try:
                value = float(row[metric])
                if value < 0 or not (value < float('inf')):
                    raise ValueError()
            except (ValueError, TypeError, KeyError):
                rejected += 1
                continue
            buckets[fmt].append(value)
    summary = {fmt:{"n":len(v), "median":statistics.median(v), "mean":round(statistics.mean(v),2)} for fmt,v in sorted(buckets.items())}
    eligible = {fmt:x for fmt,x in summary.items() if x["n"]>=min_n}
    # Without a like-for-like comparison between >=2 formats we cannot claim a winner.
    if len(eligible)>=2:
        winner = max(eligible, key=lambda fmt: eligible[fmt]["median"])
        confidence = "PROVISIONAL: account-specific historical metric; consider content category and goals"
    else:
        winner = "UNKNOWN / TEST NEEDED"
        confidence = "INSUFFICIENT_COMPARABLE_FORMATS"
    return {"account_id":account_id,"metric":metric,"category":category or "ALL_CATEGORIES", "min_n":min_n,"summary":summary,"winning_format":winner,"confidence":confidence,"rejected_rows":rejected,
            "caveat":"Historical results are not proof of causal format performance; compare like-for-like topic/date/audience and goal metrics. Reposts excluded. Never use these metrics as character counts."}

def main(argv=None):
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--csv',required=True,help='Private account export; never commit to public repository')
    p.add_argument('--account-id',required=True)
    p.add_argument('--metric',choices=VALID_METRICS,default='views')
    p.add_argument('--category',default='')
    p.add_argument('--min-n',type=int,default=5)
    args=p.parse_args(argv)
    if args.min_n<2:
        p.error('--min-n must be >=2')
    try:
        result=summarize(args.csv,args.account_id,args.metric,args.category,args.min_n)
    except (ValueError,OSError) as e:
        print(str(e),file=sys.stderr);return 1
    print(json.dumps(result,ensure_ascii=False,indent=2));return 0
if __name__ == '__main__':
    sys.exit(main())
