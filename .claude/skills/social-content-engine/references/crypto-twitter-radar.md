# Crypto Twitter Radar — on demand only

A question such as “今天 CT 有什么热点？” or “What's happening on Crypto Twitter today?” triggers **immediate** research and a fully sourced report. Do not set up a timer, schedule or background task; don't ask for credentials before trying live search.

## Sources

1. **First:** Search currently accessible public X posts using legitimate real-time web/X search tools. Search for crypto-specific topics and current posting dates. Require real x.com / twitter.com post links. A search snippet without an original X URL is not sufficient evidence of a CT hotspot.
2. **Optional:** If an authorized read-only official X API token is *already configured*, call `scripts/ct_radar.py collect` and `rank` for wider public recent-search coverage. This does not use an X login and is not necessary to begin an ordinary query.
3. **User supplied:** Work from public X links or JSON records provided by the user, verifying posting times where possible. Label input as user-provided. Synthetic test fixtures must never be described as current CT discussion.
4. **No verified posts:** Report `NO_VERIFIABLE_X_POSTS` and explain why. Do not quietly fill the report with general crypto news, old viral posts, fake links or invented metrics.

## Scope and time

- **Today** = the user's local date from 00:00 through the lookup time; show date, timezone and cutoff. **Last 24h** = rolling 24-hour window. Specify the timezone chosen if unknown.
- CT topics can include BTC/macro, ETH/L2, DeFi, stablecoins, memes/token launches, AI x Crypto, onchain market trends, security incidents and crypto-specific policy, but **only when real X authors are discussing them**. Search English and Chinese CT when accessible. Skip categories with no evidence.
- Prefer at least two independent X authors discussing the same topic, with X URLs and posting times; group duplicates and mark a lone post `SINGLE-POST SIGNAL`. Do not label an X search sample as an official Trending Topic ranking.
- Distinguish an X author's *claim* from an independently verified event, a contested assertion and your own interpretation. News articles can be used to verify a fact, never as a substitute for X-post evidence.

## Report format

Provide 5–10 actual evidenced topics when possible, fewer when not. Header shows date/timezone, lookup cutoff, source method and coverage limitation.

For each topic give: **what CT is debating**, **original X post links and timestamps** (ideally independent authors), **why the discussion matters**, **what is verified vs uncertain**, and **one independent content angle**. Never copy the original post as the user's voice. Finish with 2–3 subjects worth deeper attention, without treating suggestions as the author's beliefs.

## Optional manual API helper

```bash
python3 .claude/skills/social-content-engine/scripts/ct_radar.py collect \
  --topics examples/topics.example.json --hours 24 --max-queries 6 --per-topic 10 \
  --output data/private/ct-posts.json
python3 .claude/skills/social-content-engine/scripts/ct_radar.py rank \
  --input data/private/ct-posts.json \
  --output reports/private/radar.json --markdown reports/private/radar.md
```

These read-only commands require legitimately configured API access and may incur charges. They are *optional* for interactive radar and never run automatically. Reports and credentials stay private; no automated website logins, likes, follows, or posting.
