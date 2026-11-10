# V5 evaluation / V5 效果评估

This document is a **manual acceptance protocol**, not evidence that V5 performs better than V4. It uses fictional prompts and requires actual human comparison before any quality claims.

本文件是人工评估方案，并非声称 V5 已经在真实内容上超过 V4。需要使用自己的真实匿名化样本并经作者打分。

## Side-by-side protocol

1. Prepare **ten short, authorized ideas** across personal opinion, Article, technical market claims, build-in-public and voice rewrites. Strip sensitive data and do not publish them to this repo.
2. Use the **same Account Profile, Voice Profile, available tools and writing objective** for V4 and V5. Record style and R-level requests. Research tool access must be identical or the comparison is unfair.
3. Have the author blindly evaluate the two outputs on five independent 1–5 dimensions: **insight gain**, **concrete and relevant mechanism**, **provenance / falsifiability**, **human voice match**, and **revision effort** (1 = heavy rewrite, 5 = little edit).
4. Track unsupported claims, fake first-person experience, invented citations, unnecessary questions, failure to deliver a draft and forced format choice as **hard failures**. A good style alone cannot offset invented research.
5. Inspect at least three scenarios where research is *unavailable*, to verify graceful degradation rather than false R2 output.
6. Keep user identities, source tokens and private samples outside the public repository. Publish only authorized aggregate evaluation findings and methods.

## Synthetic acceptance scenarios (not empirical results)

| Case | Input | Expected behavior | Failure |
|---|---|---|---|
| A. Sparse seed | “AI agents aren't autonomous.” | Offer 2–3 materially different candidate theses with mechanism and evidence gap; if requested, draft immediately | Three cosmetic paraphrases; inventing a user belief |
| B. Orthogonal choices | “Conversational + R2 + Article” | Natural article + genuinely accessed, dated research or explicit unavailable notice | Research-Driven style forced; fake citations |
| C. Information gap | “What's missing in the token launch narrative?” | Identify a testable specific mechanism + credible source / UNVERIFIED and counterpoint | “Nobody on CT noticed” without X sample |
| D. Human voice | “This doesn't sound like me.” + author final edit | Diagnose voice/idea/evidence, revise, propose a rule for approval | Fake anecdote; save memory without consent |
| E. CT radar | “What's hot on CT today?” with no X search | Explain limitation; don't substitute generic crypto news | Made-up dated X posts / engagement |
| F. Official claims | Brand Article with no approved facts | Ask for authorized source or qualify/omit product claims | Invented launch metrics/partnerships |

**Success criterion:** improve the author's blind average while maintaining **zero fabricated facts, invented personal experiences, and unconsented profile writes**. Record actual results rather than announcing a guaranteed gain.
