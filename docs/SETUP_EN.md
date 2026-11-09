# English setup and usage guide

## 1. Install

**Project install (simplest):** clone/open this repository in Claude Code. The skill is under `.claude/skills/social-content-engine/SKILL.md`. Start a fresh Claude Code conversation, then ask for `/social-content-engine` or write a normal request about your voice or X content.

**Personal install (available in other local projects):** copy the whole `.claude/skills/social-content-engine` folder into `~/.claude/skills/social-content-engine`. Do not copy just `SKILL.md`, because it loads the accompanying references and script. Do not put nested copies such as `social-content-engine/social-content-engine/SKILL.md`.

## 2. Build your own voice card

```text
/social-content-engine
These 12 posts are MY writing; the next three are reference authors, not mine.
Distill my evidence-based writing style, reasoning habits, tone, and editing preferences.
Build a provisional private voice card and a sample post for me to approve.
Do not store any personal profile or samples in a public repository.
```

With no samples, the skill can draft first in a provisional style. Explicitly approve any persistent storage and its location.

## 3. From one thought to X copy

```text
/social-content-engine
Thought: There's a difference between an AI agent participating in a market and operating the issuer.
Challenge weak assumptions, suggest two angles, then write one concise English post in my own tone.
```

For a thread: `Write a 5-post thread, each post independent enough, with dates and references outside the publishable copy.`

## 4. Run a radar with the official X API

The script requires Python 3.10+ and a legitimately obtained X API Bearer token that is authorized for **recent public-post search**. Token and service costs/quotas depend on X and may change. Configure the token in your **private environment**, not a prompt or GitHub file. The script does not read passwords/cookies and cannot access your personal Following feed.

From this repo's root:

```bash
python3 .claude/skills/social-content-engine/scripts/ct_radar.py collect \
  --topics examples/topics.example.json --hours 24 \
  --max-queries 6 --per-topic 10 \
  --output data/private/ct-posts.json
python3 .claude/skills/social-content-engine/scripts/ct_radar.py rank \
  --input data/private/ct-posts.json \
  --output reports/private/radar.json \
  --markdown reports/private/radar.md
```

Review the source URLs and factual claims. Then ask Claude:

```text
/social-content-engine
Read reports/private/radar.md, verify the original sources and the event dates where possible,
and pick the two angles that best fit my OWN approved voice profile. Highlight counterarguments.
Draft one short X post only after distinguishing verified facts from social claims.
```

### No API token?

Use user-provided source data and the **offline** `rank` command. A deterministic, clearly fictional test dataset is included:

```bash
python3 .claude/skills/social-content-engine/scripts/ct_radar.py rank \
  --input tests/fixtures/posts.synthetic.json --now 2026-11-09T00:00:00Z \
  --output reports/private/demo.json --markdown reports/private/demo.md
```

This demo is NOT fresh Crypto Twitter data and must not be published as a daily brief.

## 5. Opt into a daily Claude Code cloud job

1. Confirm you have access to Claude Code cloud scheduled jobs (`/schedule`) and that its execution environment has a private authorized API secret and outbound access to `api.x.com`.
2. Open this repository in Claude Code and provide the contents of `routines/daily-radar.prompt.md` to `/schedule`. Ask for **10:00 Asia/Kuala_Lumpur daily** (or your own timezone). Confirm actual next-run time in the app, not just the text of the prompt.
3. Before enabling recurrence, run a manual trial and check the outcome. `NOT_CONFIGURED` indicates that the cloud job cannot access an API token. Local shell configuration does not automatically travel to the cloud.
4. Keep the output private. Never open public PRs with X datasets, private profile cards, or credentials. Never auto-post or bulk engage.

Scheduled jobs depend on available Claude Code capabilities; the skill cannot enable them by itself. If you use another environment, a private operating-system scheduler can invoke the same commands, with secrets kept out of the public repository.

## 6. Troubleshooting

| Symptom | What to do |
|---|---|
| Skill not found | Open the repository root in Claude Code or copy the entire folder to `~/.claude/skills`; restart the session |
| `X_API_BEARER_TOKEN is not configured` | Add a genuine read-only API token to the authorized runtime's secret store; never paste it into chat |
| HTTP 401 / 403 | Confirm token permissions and access to recent-search endpoint |
| HTTP 402 | Review X's developer billing / credits, and whether the endpoint is available to your plan |
| HTTP 429 | Respect rate limits; reduce queries; do not bypass limits |
| Empty report | Verify date window, source queries, input data and API permissions; do not fill it with invented posts |
| Daily cloud job sees no token | Configure the token in the *cloud job's* environment; local Claude or X browser login is not sufficient |
| Text is not in your voice | Supply authentic author posts and explicit edits, ask for a calibration, and approve private saving |

## 7. What this does not do

- It does not log into X using your browser session.
- It does not collect personalized/private home-feed posts, bookmarks or DMs.
- It does not auto-post, auto-reply, like, follow, or schedule publications.
- It does not imply that a high-scoring post is true or universally trending.

The user is responsible for X API usage/fees and checking the current policies.
