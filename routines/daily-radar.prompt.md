# Daily Crypto Twitter Radar — paste into Claude Code /schedule

Suggested schedule: **09:00 Asia/Kuala_Lumpur daily** (edit to your timezone). **Do not create this schedule until the owner configures authorized read-only X API access** in the execution environment and has approved billing. The job will not automatically sign in to a browser/X account.

---

You are running a user-authorized, **read-only** daily Crypto Twitter discussion radar using the `social-content-engine` Skill loaded from `.claude/skills/social-content-engine/`.

1. Determine today's current date in Asia/Kuala_Lumpur. Search a 24-hour window for meaningful Crypto Twitter discussions: BTC/macro, Ethereum/L2, DeFi/stablecoins, memecoin/token launches, AI agents, infra/security, and relevant 中文 CT. Do not force every category into the output.
2. Use `python3 .claude/skills/social-content-engine/scripts/ct_radar.py collect --topics examples/topics.example.json --max-queries 6 --per-topic 10 --hours 24 --output data/private/ct-posts.json` **only if** the job's authorized execution environment has `X_API_BEARER_TOKEN` and network access to api.x.com. Do not print or display any token. No automated browser login or scraping, and no fallback to a session cookie.
3. If no credentials or no source data, report **NOT_CONFIGURED / NO_VERIFIED_INPUT** with the needed setup, and STOP. Do not invent trends or cite unverified posts.
4. Rank data via `python3 .claude/skills/social-content-engine/scripts/ct_radar.py rank --input data/private/ct-posts.json --output reports/private/radar.json --markdown reports/private/radar.md --limit 6`.
5. Read the ranked report, review original sources via legitimate access if available, and independently verify any important underlying news. Deliver up to SIX *actual evidence-backed* CT discussion signals (less if insufficient). Each must show topic, source URL, post and event date if confirmed, why it matters, one possible original personal-content angle, a counterargument or caveat and confidence (high/medium/low). The Python score is not proof a story is real or universally trending.
6. Provide a concise **Top 2 writing opportunities for this author's interests**, if their personally approved profile is accessible. Otherwise do not assume their opinions or persona.
7. Draft-only. Never post, reply, DM, like, follow, manipulate trends or modify social accounts. Never save or commit raw X exports, credentials, personal profiles or reports to a public GitHub repository. Results remain in this private routine's output and ignored local files, if the cloud environment retains them. Do not open a public PR with the report.

End with an honest source status line, the cutoff time and each source URL. If the job has not been configured by its owner, do not claim it was scheduled or run.
