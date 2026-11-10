# Social Content Engine

**账号定位 · 个人风格蒸馏 · 深度观点 · Research · X 内容创作 · CT Radar**

**Account Positioning · Voice Distillation · Insight Expansion · Research · X Writing · Crypto Twitter Radar**

[中文](#中文) · [English](#english) · [MIT License](LICENSE)

---

## 中文

**你提供一个想法，Skill 帮你把它想得更深、查得更实在，再写成真正像你自己的内容。**

Social Content Engine 是免费的开源 Claude Code Skill。它不是把一句话拉长的 AI 文案生成器，而是一个兼顾**个人表达、内容判断和可信研究**的写作伙伴。主题不只限于 Crypto；CT Radar 则专门研究 Crypto Twitter 的真实讨论。

### 1. 先对齐账号，再选择内容角度

建立私有的 **Account Profile**（账号定位、受众、内容支柱、词汇、明确立场和红线），关联独立的 **Voice Profile**（你怎么写）。公司或项目账号可以设置 **approved-source register**，明确哪些官方资料被批准对外使用。

**账号档案第一行回答：什么格式在这里真正有效？** 比较自己账号的历史数据，而不是默认短推或 Thread。支持 **Article、Long Post、Short Post、Thread**；Article 是有标题、章节、论证与来源的独立长文章，不是放大的短推。没有数据时写 `UNKNOWN`，不杜撰效果。若有个人号和官方号，可自定义谁首发观点/故事，谁首发教程/公告，避免重复转发。

### 2. Voice Distillation：让文字更像你

建议提供 **8–20 条自己写过的推文或文章**和你对 AI 草稿的修改记录。Skill 会提炼语气、开头、句式、论证方式、细节偏好与 **Humanity Fingerprint**：你经常从哪里发现问题、如何保留不确定性、讨厌哪些 AI 腔句子。参考作者只用于学习广义写作技巧，不照搬其独特表达。

```text
/social-content-engine
这是我自己写过的 10 条推文：[粘贴]
请建立 Voice Profile 和 Humanity Fingerprint，找出哪些表达真正像我，
并根据我的想法写一条校准推文。不要模仿参考作者。
```

个人档案和修改记录默认不写入公开仓库；持续保存前须征得本人同意。

### 3. 从一句笼统观点，发展出真正有信息量的内容

输入可以很短，例如：「AI Agent 还没有真正的经济自主权。」

**Idea Expansion** 会先区分作者已经认可的观点与 Skill 提议的方向，尝试挖掘**权力归属、责任分配、经济激励**等不同机制，找出反例、现实影响和需要核实的证据。它不再只把原话修饰成“不是 A，而是 B”。若你明确要求直接成稿，它仍会在当前对话给出草稿，不强制经过选择流程。

你可以选择这篇内容的表达方式（**Writing Mode**）：

| 模式 | 风格和适用场景 |
| --- | --- |
| **Professional｜专业分析** | 克制准确，适合行业、公司或产品分析 |
| **Conversational｜轻松交流** | 像真实对话，适合个人观察和讨论 |
| **Research-Driven｜研究驱动** | 方法、来源和不确定性清楚，适合深度 Article |
| **Opinionated｜鲜明观点** | 有立场也考虑反驳，适合个人观点和 QRT |
| **Builder's Notes｜实践笔记** | 从真实操作、约束与复盘出发，适合 Build in Public |

**Writing Mode 只是本次表达方式，不会覆盖账号定位或作者原本的观点。** 没有指定时，Skill 会根据账号和内容推荐一种，并仅在确实有必要时询问。

### 4. 可选 Research：不只是“贴几个链接”

研究深度独立于表达风格，例如你可以用 **轻松交流 + R2 深度研究 + Article**。

| 深度 | 会做什么 |
| --- | --- |
| **R0 · Original Thinking** | 基于你的想法推理，不进行额外的广泛研究；重要事实仍需核实或注明不确定 |
| **R1 · Evidence Supported** | 尝试查证 1–3 条有价值的支持或反驳证据 |
| **R2 · Deep Research** | 多来源交叉核验，追溯原始数据、机制、反例和方法局限 |

**Information Gap Mining** 会尝试找真正值得注意的细节：合约权限、激励机制、实际使用与叙事落差、数据定义等。每个重要发现会关联来源、时间和可信状态；不因为“看起来少人知道”就宣称 CT 都没注意到。**Research 只有在实际访问并检查来源后，才会被标为已完成。**

### 5. 日常怎么用？

**简短想法 → 更丰富的观点 → 写作：**

```text
/social-content-engine
我的观点：AI Agent 还没有真正的经济自主权。
请先提出三个不同的潜在分析角度，指出各自的机制、反例和信息缺口。
我倾向 Research-Driven，但希望文字自然。Research 使用 R1。
推荐最有价值的方向，做必要的来源核实，再写成一篇英文 Article。
不要编造我亲身做过的事，也不要把建议的角度当成我认同的结论。
```

**有人味的改写：**

```text
/social-content-engine
这篇草稿太像 AI，请按我的 Voice Profile 做 Human Voice Editor：
保留真实观点，删除套路对比句和无信息量的开头；
指出内容本身缺少什么机制或事实。不要凭空加入个人经历。
```

**当天 CT 热点（仅按需，不自动运行）：**

```text
/social-content-engine
今天 Crypto Twitter 上真正讨论的热点有哪些？
只要 CT 相关的 Crypto 话题，给我最多 5–10 个有实际原帖证据的主题，
包括 X 链接、时间、不同观点、值得追查的信息差和可以写的角度。
```

如果当前环境没有可用的实时 X 搜索/合法来源，Skill 会说明限制，不会用普通新闻冒充 CT 热点，也不会自动登录、抓取账号或发推。

### 6. 安装（Claude Code）

**直接使用：** 在 Claude Code 中打开本仓库，Skill 位于 `.claude/skills/social-content-engine/`。开启新的会话，输入 `/social-content-engine` 即可。

**安装到个人目录（Mac / Linux）：**

```bash
git clone https://github.com/caelynmoss/social-content-engine.git
mkdir -p ~/.claude/skills
cp -R social-content-engine/.claude/skills/social-content-engine ~/.claude/skills/
```

Windows：复制整个 `.claude/skills/social-content-engine` 到 `%USERPROFILE%\.claude\skills\`，确保有 `SKILL.md`，重新开启 Claude Code。

[中文详细说明](docs/SETUP_ZH.md) · [V5 评估方式](docs/V5_EVALUATION.md) · [隐私与安全](docs/SECURITY.md)

---

## English

**Bring a rough idea. Develop a real insight, check what matters, then write something that sounds like you.**

Social Content Engine is a free, open-source Claude Code Skill combining **account positioning, personal voice, editorial thinking, evidence-backed research, writing, and on-demand Crypto Twitter discovery**. Its writing topics are unrestricted; the CT Radar covers genuine crypto discussions on X only.

### 1. Account before content

Use a private **Account Profile** for editorial positioning, audience, vocabulary, approved stances, red lines, format evidence and an approved-source register for official claims. Keep a separate **Voice Profile** for how the author writes.

The first line should say **what format actually works for this account**, based on its real post performance, or `UNKNOWN`. Support **Article, Long Post, Short Post and Thread** as distinct formats. An Article is a full original piece with a title, sections, argument and sources—not a padded tweet. Personal and official accounts can specify original-content routing to avoid duplicative reposts.

### 2. Voice Distillation and the Humanity Fingerprint

Share **8–20 authentic posts** you wrote and, optionally, edits to earlier AI drafts. The Skill learns your structure, rhythm, reasoning, humor, uncertainty and the expressions you routinely remove. Peer creators only supply general writing craft, never their distinctive language or opinions.

```text
/social-content-engine
Here are 10 posts written by me: [paste]
Build my Voice Profile and Humanity Fingerprint from real samples.
Write one calibration post. Don't imitate reference creators.
```

Private profiles are never saved persistently or uploaded to public GitHub without your permission.

### 3. Adaptive Idea Expansion + five Writing Modes

Short input no longer means shallow output. **Idea Expansion** tests mechanisms, counterexamples, practical stakes and evidence gaps, proposing **2–3 genuinely different potential angles** without pretending that the user already believes them. An explicit “just draft it” still gets a useful draft immediately.

| Mode | Best for |
| --- | --- |
| **Professional** | Precise, restrained sector or institutional analysis |
| **Conversational** | Real, natural personal observations and discussion |
| **Research-Driven** | Method-aware, evidence-rich explanations and Articles |
| **Opinionated** | Sharp, defensible takes without manufactured outrage |
| **Builder's Notes** | Documented implementation trade-offs and learnings |

The mode describes **this piece**, not the writer's personality or research effort. It remains separate from the output format and research depth.

### 4. Optional R0 / R1 / R2 research + Information Gap Mining

- **R0 · Original Thinking:** No extra broad research; material factual claims still need verification or qualification.
- **R1 · Evidence Supported:** Seek 1–3 relevant, trustworthy findings that strengthen or challenge the thesis.
- **R2 · Deep Research:** Triangulate primary evidence, dated background, data definitions, counterevidence and limitations.

**Information Gap Mining** seeks details that change a real reader's decision, such as onchain authority, liquidity control, incentives or discrepancies between usage and narrative. Keep an **Evidence Ledger** that distinguishes verified evidence, source claims, disputes, hypotheses and author interpretation. Never label something “ignored by CT” without sampling relevant X discussion, and never claim to have researched sources that were inaccessible.

### 5. Try it

**From one sentence to a sourced Article:**

```text
/social-content-engine
My idea: AI agents may not yet have meaningful economic autonomy.
Find three materially different possible angles with mechanisms and counterexamples.
Use Research-Driven prose with R1 evidence support and recommend the strongest angle.
Then write a substantial English Article in my voice. Don't manufacture my experiences
or treat your suggested angle as my pre-existing belief.
```

**Human-sounding revision:**

```text
/social-content-engine
This draft reads like AI. Use my Voice Profile to edit out generic hooks,
formulaic contrasts and filler. Keep my actual viewpoint and identify missing facts.
Never invent a first-person story.
```

**On-demand CT radar:**

```text
/social-content-engine
What are today's Crypto Twitter hotspots? Find up to 5–10 crypto conversations
with real dated X post links, independent viewpoints and possible information gaps.
```

There is **no scheduled or automatic radar**. This is not X's official Trending Topics list (not X Trending Topics ranking); the Skill never performs browser login. No X web automation is performed. Search access may be limited; it reports missing original X evidence rather than inventing trends.

### 6. Install with Claude Code

Open this repository in Claude Code, then use `/social-content-engine`. For use across projects on Mac/Linux:

```bash
git clone https://github.com/caelynmoss/social-content-engine.git
mkdir -p ~/.claude/skills
cp -R social-content-engine/.claude/skills/social-content-engine ~/.claude/skills/
```

On Windows copy `.claude/skills/social-content-engine` to `%USERPROFILE%\.claude\skills\`, then restart Claude Code.

[English setup](docs/SETUP_EN.md) · [V5 evaluation](docs/V5_EVALUATION.md) · [Security](docs/SECURITY.md) · [MIT License](LICENSE)
