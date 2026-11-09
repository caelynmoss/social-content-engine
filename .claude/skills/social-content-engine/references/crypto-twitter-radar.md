# Daily Crypto Twitter Radar (read-only)

The user may ask for 5–8 daily CT discussion signals, topics for original writing, or analysis of posts they personally collected. The Radar is **separate from personal voice**, and it does not auto-post.

## Source precedence

1. **X official API (preferred for automation):** Use `scripts/ct_radar.py collect` only with an explicit, authorized `X_API_BEARER_TOKEN` in the runtime environment, subject to X API terms, cost controls and rate limits. The API reads **public recent search results**, not the user's authenticated home feed. A personal X password, cookies or browser session is never needed.
2. **Manually curated X posts:** The user may provide public links and pasted excerpts or an exported JSON list. Run `rank` against that data, labelled `user-provided`. Links alone cannot establish created_at or metrics; retrieve them via authorized means or mark missing and do not fabricate them.
3. **Public web/news research:** Good for checking whether an X claim corresponds to a real event, not a substitute for a purported X activity count or an automated X feed.
4. If no usable source exists: output `NOT CONFIGURED / NO VERIFIED INPUT`, explain how to connect an API or provide sample records, and do **not** invent five trending topics.

**Do not implement unattended browser scraping, scripted logins, cookie extraction, password storage, proxy rotation, rate-limit bypass, automated Likes, follows, retweets or posting.** X's 2026 automation rules prohibit non-API automation of its website. Claude-in-Chrome can use the user's logged-in browser in an *interactive session* subject to website rules, but never assume its presence or turn it into an unattended site scraper. Prefer a user copying selected URLs/records if no API token is available.

## Method

1. Determine today's date and a 24-hour lookback in the user's time zone, default Asia/Kuala_Lumpur only if provided as a preference. Use UTC source timestamps, keep an explicit cutoff. The API supports recent search of the past seven days; the provided script defaults to the previous 24h.
2. Collect up to six topic searches by default, ten posts per search (60 possible records before dedup), or within the user's approved budget. Search concepts across AI x crypto, BTC/macro, ETH/L2, DeFi/stables, launches/memes, security/regulation, and optionally Chinese CT. Topics may be customized in `examples/topics.example.json`.
3. Preserve post ID, canonical URL, created_at, author if returned, read timestamp, metrics, and source. Deduplicate by post ID and near-duplicate text; rank by bounded freshness + engagement heuristic, with category diversity. The score is **not** an official X Trending score, not proof of a claim, and not a perfect bot filter.
4. Recommend 5–8 useful discussion signals **only when data supports that many**. Each needs a source URL, date, summary, reason worth monitoring, and one authentic possible angle for that author's interests. Cite at least two independent posts or external reporting for claims of an *industry-wide trend* where possible; if not, label it `SINGLE-POST SIGNAL`.
5. Pressure-test rumor, bait and price predictions. Clearly distinguish **X POST CLAIM**, **INDEPENDENTLY VERIFIED EVENT**, and **EDITORIAL HYPOTHESIS**. Do not call every high-engagement post a news event.
6. Use the author's private profile only when drafting a follow-up. A good Radar may cover many topics; the writer should choose a specific fit rather than force every development into crypto marketing.
7. Output 5–8 concise cards (or fewer), grouped only if evidence supports common events. Add an optional `Best fit for your voice` and `What would disprove this take` when a profile is available. Reports and profiles are private and must **not** be committed to this public repository.

## Commands

From the public repository root:

```bash
# First: configure a legitimate X API credential in your private runtime environment.
python3 .claude/skills/social-content-engine/scripts/ct_radar.py collect \
  --topics examples/topics.example.json --max-queries 6 --per-topic 10 \
  --output data/private/ct-posts.json

python3 .claude/skills/social-content-engine/scripts/ct_radar.py rank \
  --input data/private/ct-posts.json \
  --output reports/private/radar.json --markdown reports/private/radar.md
```

`rank` has **no network access** and works with user-provided JSON. `collect` fails explicitly on a missing token, API 401/402/403/429, or network failure; it never falls back to a fake feed. A bounded API request can incur charges. User must configure X credits/rate limits and approve automation.

### Output shape

`{ "status": "OK", "source": "x-api-recent-search", "collected_at": "...", "posts": [{ "id": "123...", "created_at": "...", "text": "...", "public_metrics": { "like_count": 12, "retweet_count": 2 }, "author_id": "..." }] }`

`rank` produces `.json` and `.md` with sourced discussion signals. The LLM should use those records for synthesis, counterpoints, independent research and personalized drafts; the Python heuristic alone does not generate verified news or intelligent arguments.

## Scheduling

The Skill itself **does not run every day automatically**. A user can opt into Claude Code's `/schedule` cloud jobs, which execute using that job's authorized environment/credentials, or can run their own local OS scheduler. A local X token is **not** magically available to Claude Code's remote job. See `routines/daily-radar.prompt.md` and the bilingual setup docs for exact steps.
