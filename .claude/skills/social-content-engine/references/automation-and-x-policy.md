# X policy, credentials and unattended task guardrails

Official sources (verify current versions before deploying):
- https://help.x.com/en/rules-and-policies/x-automation — updated April 2026: warns against non-API website scripting, rate-limit evasion, unsolicited automated interactions and trending-topic manipulation.
- https://docs.x.com/x-api/posts/search/introduction — recent search endpoint `GET /2/tweets/search/recent` and seven-day window.
- https://docs.x.com/x-api/getting-started/pricing — pay-per-use X API credits; verify prices in developer console.
- https://claude.com/resources/articles/introducing-routines-in-claude-code — Claude Code `/schedule` cloud routine functionality.
- https://code.claude.com/docs/en/chrome — Claude-in-Chrome interactive, visible browser integration, not a guarantee of unattended X access.

Rules:
- API is read-only; no posting or modifying a social account. For authenticated *private* timeline/bookmarks or user context, build a separately consented official OAuth integration; that capability is **not** in this version. Do not ask for an X username/password.
- Keep token in private environment/secrets only, never in prompts, committed files or reports. Use a dedicated read-scoped token; revoke after a leak.
- Respect the API's returned 429 rate limits and billing rules; do not rotate accounts or endpoints to evade limits. The script deliberately makes at most `--max-queries` bounded requests, no auto-retry loops.
- If a cloud task has no API credential/network permission, return NOT_CONFIGURED and explain; never fake results or assume it accessed the user's X account.
- Do not publish daily source text, identifiable audience lists, personal voice profiles, or X exports as GitHub commits or public PRs. Output should remain in a private job result or ignored local report directory.
- Research is not posting. No scheduled publications or coordinated engagement; author reviews every piece of copy.
- Respect each platform's API and copyright terms when storing excerpts or redistributing data.
