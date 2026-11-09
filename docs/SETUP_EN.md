# English setup and usage

## 1. Install

Open the GitHub repository in Claude Code; the Skill is at `.claude/skills/social-content-engine/SKILL.md`. To use it across your local projects, copy the entire folder into `~/.claude/skills/social-content-engine/` (Windows: `%USERPROFILE%\.claude\skills\social-content-engine\`) and restart Claude Code.

## Account alignment and evidence-led formats

Build a separate private Account Profile first: audience promise, editorial lens, explicit stances, vocabulary, red lines, source approval registry and optional linked-account routing. Put the account's actual winning format on the **first line**, with sample size, window and performance metric. ARTICLE, LONG_POST, SHORT_POST and THREAD are all valid; weak evidence means UNKNOWN, not a guessed winner.

An ARTICLE is a full long-form draft with sections, reasoning and sources. It is distinct from a thread or a long single post. Confirm native publishing eligibility separately. Optional personal/official routing helps prevent duplicative reposts: opinions and stories can originate personally; approved tutorials, data and partnerships should originate officially.

Blank private templates are under the Skill's assets/ directory. A local CSV format comparison is available via scripts/format_audit.py --help. Keep authorized source records and account data out of public GitHub.
## 2. Ask for Crypto Twitter hot topics today

```text
/social-content-engine
What are today's Crypto Twitter hotspots?
Give me up to 5–10 genuine conversations on X about crypto,
with original post links, timestamps, corroborating independent authors,
what is unverified, why it matters and an original writing angle.
```

**There is no recurring job or automatic startup.** The user actively asks whenever they want a report. The Skill uses whatever authorized live X/web search is available; if it cannot access actual dated X posts, it states the limitation rather than inventing news or substituting general articles.

"Today" means midnight to query cutoff in the user's local time zone; "past 24 hours" is a rolling window. Specify timezone, cutoff and source coverage. Evidence from multiple independent X posters is stronger than an isolated post.

## 3. Make a post in your voice

```text
/social-content-engine
Take topic #2 from today's radar, challenge the premise
and write one short English X post in my voice without copying the original.
```

The user may supply 8–20 authentic own posts for Voice Profile calibration. Storing any personal profile persistently requires explicit consent.

## 4. Optional manually invoked X API

With authorized X public recent-search access and suitable credits, keep `X_API_BEARER_TOKEN` private and manually run:

```bash
python3 .claude/skills/social-content-engine/scripts/ct_radar.py collect \
  --topics examples/topics.example.json --hours 24 --max-queries 6 --per-topic 10 \
  --output data/private/ct-posts.json
python3 .claude/skills/social-content-engine/scripts/ct_radar.py rank \
  --input data/private/ct-posts.json \
  --output reports/private/radar.json --markdown reports/private/radar.md
```

The API is not required before a normal interactive query, and the script never runs automatically. An offline ranking also accepts user-supplied real X post JSON. Synthetic test records are never live CT evidence.

## 5. Safety

No invented CT links, counts or timestamps. No X passwords, cookies, automated browser login, website scraping, background tasks or auto-posting. Don't commit API credentials, real personal style profiles or X exports to a public repository. Review all drafted posts before publication.
