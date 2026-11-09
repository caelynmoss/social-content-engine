# Social Content Engine

**A personal X writing partner + an opt-in, read-only Crypto Twitter radar.**

[中文说明 / Chinese guide](README.zh-CN.md) · [English setup](docs/SETUP_EN.md) · [中文安装教程](docs/SETUP_ZH.md) · [Security](docs/SECURITY.md)

Social Content Engine is an open-source Claude Code skill for turning rough thoughts into thoughtful, source-aware short posts, long posts, and threads **in the author's own voice**. It can also identify a handful of fresh Crypto Twitter (CT) discussion *signals* each day from the official X API or author-provided post data, then help connect those signals to an original argument. It is not a generic marketing calendar or an auto-post bot.

### What it does

- **Distill your own voice:** learn from writing you actually authored and corrections you approve; keep each author's profile separate. Reference creators supply high-level craft, not copied language or borrowed opinions.
- **Think with you:** question weak logic, expose overlooked mechanisms, surface a defensible angle, and distinguish facts from your conclusions.
- **Draft in your format:** one concise X post, an eligible longer post, or a coherent thread, in Chinese or English.
- **Daily CT radar (opt-in):** sample recent **public posts** through the **official X API**, deduplicate and rank by a documented freshness/engagement heuristic, then let Claude verify and interpret a shortlist of signals.
- **Manual/offline fallback:** rank user-supplied post records without API credentials. No sources? No fabricated trends.

> **Important:** The radar returns sampled *discussion signals*, **not X's official Trending Topics**, an exhaustive CT ranking, or independently verified news. Posts can be misleading. The agent should verify key factual claims before drafting. Installing the skill does **not** create a scheduled job or log in to your X account.

## Quick start: Claude Code

Clone or open this repository as your Claude Code project. The skill is already at `.claude/skills/social-content-engine/SKILL.md` and can be discovered from inside this project. Alternatively, copy that **entire** directory to `~/.claude/skills/social-content-engine/` for use in your other projects. Reopen your Claude Code session.

Try:

```text
/social-content-engine
Here is my thought: AI agents are getting better at following instructions, but that is not the same as becoming independent issuers.
Pressure-test the reasoning, then write one short X post in my voice. Don't invent sources.
```

To build an individual voice profile, paste 8–20 of **your own** past posts (3–5 for a provisional profile), and optionally separately labelled reference writers. Ask the skill to return a calibrated voice card. Private profiles stay on your machine, **not in this repository**.

For exact copy/paste setup, commands, daily-job requirements and common failures, see [English setup](docs/SETUP_EN.md) or [中文使用指南](docs/SETUP_ZH.md).

## Crypto Twitter radar: two ways to feed it

**A. Official X API (for authorized automation):**

Configure a **read-only X API Bearer token** privately as `X_API_BEARER_TOKEN` and check API product access, costs and rate limits before running. A token for public-post search does **not** require handing the skill your X username or password, and it does **not** give it access to your personalized Following feed.

```bash
python3 .claude/skills/social-content-engine/scripts/ct_radar.py collect \
  --topics examples/topics.example.json \
  --output data/private/ct-posts.json
python3 .claude/skills/social-content-engine/scripts/ct_radar.py rank \
  --input data/private/ct-posts.json \
  --output reports/private/radar.json \
  --markdown reports/private/radar.md
```

**B. User-provided data (no API or automation):**

Provide a JSON file with publicly sourced posts including real post IDs, ISO UTC `created_at`, text and optional metrics. Then run `rank --input <your-private-file>`. A sample *synthetic* input is in `tests/fixtures/posts.synthetic.json` (do not portray its entries as real trends).

```bash
python3 .claude/skills/social-content-engine/scripts/ct_radar.py rank \
  --input tests/fixtures/posts.synthetic.json \
  --now 2026-11-09T00:00:00Z \
  --output reports/private/example.json \
  --markdown reports/private/example.md
```

The Python tool is **read-only** and uses the standard library. It sends only bounded GET requests to `api.x.com`; it does **not** publish or act on X. A missing API key produces a clear error rather than fake data.

## Daily scheduling with Claude Code

Claude Code has cloud scheduled tasks via `/schedule` in eligible environments. **No job is activated by this repository.** After you have configured authorized X API access *in the scheduled job's cloud environment*, create a private scheduled job based on [routines/daily-radar.prompt.md](routines/daily-radar.prompt.md). For example, ask `/schedule` to run the prompt **daily at 10:00 Asia/Kuala_Lumpur**. Confirm the job's timezone, secret configuration, repository access, and next-run time in the Claude UI.

Do not assume the cloud session has your local environment variables or a logged-in X browser. If the token or paid API access is missing, the job must report `NOT_CONFIGURED` and **must not** claim it collected X posts. Never open a public pull request with private reports. See [automation restrictions](.claude/skills/social-content-engine/references/automation-and-x-policy.md).

## Security and boundaries

- No X web automation, password harvesting, cookie reuse, rate-limit bypass, automated following/likes, DMs or publishing.
- Never store API keys, X exports, author writing samples, private voice profiles or real personal data in this public repository.
- News, engagement and individual posts are not interchangeable; always show source, timestamps and uncertainty.
- Users review and publish their own posts. All writing remains **draft-only**.

See [SECURITY.md](docs/SECURITY.md). The project is independently usable and does not require access to any private corporate repository.

## Repository layout

```text
.claude/skills/social-content-engine/
  SKILL.md
  agents/openai.yaml
  references/             # voice, critical thinking, sourced CT radar, safe automation
  scripts/ct_radar.py     # official X API reader and offline scoring
  assets/                 # synthetic examples and voice card template
docs/                      # English + Chinese guides and security
examples/topics.example.json
routines/daily-radar.prompt.md
tests/                     # offline, synthetic-data unit tests
```

## Validation

```bash
python3 -m unittest discover -s tests -v
python3 .claude/skills/social-content-engine/scripts/ct_radar.py --help
```

No live X data is bundled with this project and the CI tests never call X.

## License

MIT — see [LICENSE](LICENSE). Contributions and respectful security reports are welcome (see [CONTRIBUTING.md](CONTRIBUTING.md)).
