# Social Content Engine

**个人风格蒸馏 · 观点思考与内容创作 · Crypto Twitter 热点**

**Voice Distillation · Thinking Partner & X Writing · On-Demand CT Radar**

[中文](#中文) · [English](#english)

---

## 中文

**从一个简单想法，到真正有自己风格的 X 内容。**

Social Content Engine 是一款免费开源的 Claude Code Skill，包含三个核心能力：**个人风格蒸馏、观点思考与内容创作、按需 Crypto Twitter 热点研究**。不只是把一句话润色得更漂亮，而是帮助你找到值得表达的观点、理清论证，再用自己的语言写出来。

### 1. Voice Distillation｜个人风格蒸馏

很多 AI 写出的推文看起来都很像。这个功能希望解决的是：**让内容更像你，而不是更像 AI。**

首次使用时，建议提供 8–20 条自己写过的推文或文章。Skill 会从真实样本中分析你习惯的开头和收尾、语气、句子长短、论证方式、用词、幽默感以及不喜欢的表达，并整理成一份 **Voice Profile**。样本不足时也能先生成初步版本。

你也可以提供喜欢的同行或参考作者，但 Skill 只借鉴他们的结构、节奏和论证技巧，不会照搬他们的独特措辞、经历或观点。

~~~text
/social-content-engine
以下是我自己写的推文：[粘贴 8–20 条]
以下是参考作者的内容：[可选，请单独标注]

请分析我的写作习惯、语气、观点表达、句式和内容偏好，
建立 Voice Profile，然后用我的一个观点写一条校准短推。
不要复制参考作者的文字。
~~~

没有历史样本，也可以先生成内容，但会采用临时风格。你的个人档案不会自动上传公共仓库；持久保存需要你的明确同意。

### 2. Thinking Partner + Content Creation｜观点思考与内容创作

**只要有一个想法，不需要先写好完整稿件。** 可以输入一句话、几条零散观点、一段语音转写、新闻链接或已有草稿。

Skill 会根据需要：
- 找出你真正想说的判断，以及值得讨论的切入点；
- 分析逻辑漏洞、可能的反驳与现实意义；
- 在相关时查证最新新闻、数据及原始来源；
- 保留你的立场和语气，形成自然且有内容的原创表达。

支持的形式：

| 形式 | 用途 |
| --- | --- |
| Short Post | 单条短推，简洁直接 |
| Long Post | 更完整的观点分析；较长的单条 X 帖子需账号具备相应权限 |
| Thread | 把一套论证拆成有递进关系的多条推文 |
| Rewrite | 保留原意，把草稿改得更像本人 |
| Angle Exploration | 先找出不同角度、检验观点，再决定写什么 |

**一句话变短推：**

~~~text
/social-content-engine
我的想法：很多 AI Agent 仍然只是执行人的指令，
但这不等于真正的经济自主权。

帮我找到最有意思的切入角度，指出逻辑上的薄弱处，
再按我的个人风格写成一条英文短推。
不要营销腔，也不要替我编造事实。
~~~

**把想法写成 Thread：**

~~~text
/social-content-engine
我想讨论：[粘贴几个观点]
先帮我梳理逻辑、寻找反驳、必要时查证事实，
最后写成 5 条英文 Thread。每条都要推进论证，别重复。
~~~

如果输出不够像你，直接反馈「这不是我的观点」「太像 AI」「我不会这样开头」。Skill 会先修改当前内容；你同意后才会把长期偏好更新到 Voice Profile。**主题不限 Crypto：AI、创业、市场、产品、技术、生活观察都可以。**

### 3. Crypto Twitter Radar｜当天 CT 热点

想知道今天 CT 正在讨论什么，**主动问一次就够了**。不需要配置定时任务，也不会自动运行。

~~~text
/social-content-engine
今天 Crypto Twitter 有什么热点？
只要今天 X 上真实有人讨论的 Crypto 内容，给我 5–10 个重点。
每个附 X 原帖、发布时间、争论内容、为什么重要、
哪些信息尚未核实，以及一个原创写作角度。
~~~

Skill 首先尝试当前环境可用的合法实时 X/网页搜索，寻找 BTC、ETH、DeFi、Meme、AI x Crypto、链上活动和安全事件等真实 CT 讨论。**有 X 原帖才算 CT 讨论信号**；只有新闻网站报道不能冒充热点。如果来源不足，结果可能少于 5 个，并明确说明局限。这不是 X 官方 Trending Topics 排名。

已有合法 X API 公开搜索权限时，可选用只读 API 扩大采样，但这不是日常提问的前置条件。Skill 不会索取 X 密码或 Cookie，不自动登录或发推。

### 4. 安装与开始

最简单的方法：用 Claude Code 打开这个仓库。Skill 已在 .claude/skills/social-content-engine/，开始新会话即可使用 /social-content-engine。

若要在其他本地项目中使用，Mac / Linux 可以执行：

~~~bash
git clone https://github.com/caelynmoss/social-content-engine.git
mkdir -p ~/.claude/skills
cp -R social-content-engine/.claude/skills/social-content-engine ~/.claude/skills/
~~~

Windows 可把同一文件夹复制到 %USERPROFILE%\.claude\skills\。确保文件夹内有 SKILL.md，并重新打开 Claude Code。

[中文详细使用指南](docs/SETUP_ZH.md) · [安全与隐私](docs/SECURITY.md) · [参与贡献](CONTRIBUTING.md)

---

## English

**From a rough idea to an X post that actually sounds like you.**

Social Content Engine is a free, open-source Claude Code skill with three core abilities: **personal voice distillation, thinking and content creation, and on-demand Crypto Twitter research**. It doesn't just polish sentences; it helps you find an argument worth making and express it in your own words.

### 1. Voice Distillation

AI-written posts often sound the same. This feature aims to make your writing sound **more like you, not more like AI**.

Share 8–20 posts or articles you wrote yourself. The skill identifies your opening and closing habits, tone, sentence rhythm, reasoning patterns, vocabulary, humor, and writing preferences, then builds a **Voice Profile**. Fewer samples can produce a provisional profile.

You may also provide writers you admire, separately identified as references. Their work contributes high-level writing techniques, not copied distinctive lines, experiences, or opinions.

~~~text
/social-content-engine
Here are posts I wrote: [paste 8–20 samples]
Here are reference writers: [optional, clearly separate]

Analyze my tone, rhythm, argument style, openings and editorial preferences.
Build my Voice Profile and write one calibration post based on my own idea.
Don't copy the reference writers.
~~~

No samples? You can still write right away in a provisional voice. Private profiles are not automatically uploaded to GitHub or saved persistently without your permission.

### 2. Thinking Partner + Content Creation

**Start with one sentence, not a polished draft.** Bring rough notes, a voice-note transcript, a link, or something you have already written.

The skill can:
- Clarify your actual thesis and find stronger, genuinely different angles;
- Challenge weak reasoning and identify fair counterarguments;
- Check recent news and relevant evidence when useful;
- Turn the result into original copy that preserves your voice and position.

| Format | What it's for |
| --- | --- |
| Short Post | One concise X post |
| Long Post | Deeper analysis, subject to X account eligibility for longer single posts |
| Thread | A connected sequence of posts that develop one argument |
| Rewrite | Improve a draft without changing what you mean |
| Angle Exploration | Compare distinct angles before you start writing |

**One thought → one post:**

~~~text
/social-content-engine
My thought: Many AI agents still follow human instructions,
but that does not automatically make them economically autonomous.

Find the most interesting angle, challenge weak assumptions,
then write one short English X post in my voice.
No marketing filler or invented facts.
~~~

**One argument → a thread:**

~~~text
/social-content-engine
Here's my rough take: [your notes]
Help me organize the logic, consider objections, and check facts if useful.
Then make it a 5-post English thread where each post advances the argument.
~~~

Feedback such as “That's not my opinion,” “too generic,” or “I wouldn't open this way” improves the current draft. Lasting changes to your Voice Profile require permission. **Any topic is welcome**, not just crypto or AI.

### 3. On-Demand Crypto Twitter Radar

Want to know what CT is discussing today? **Just ask.** There is no recurring background task.

~~~text
/social-content-engine
What are today's Crypto Twitter hotspots?
Give me 5–10 topics genuinely being discussed on X today.
For each, include original X post links, posting times, key debates,
why it matters, unverified claims and an original writing angle.
~~~

The skill tries available authorized live X/web search first, across BTC, ETH, DeFi, memes, AI x Crypto, onchain activity, security and other crypto discussions. **A real X source is required**; generic news coverage alone does not prove a Crypto Twitter hotspot. When access is limited, the skill reports fewer topics rather than inventing posts. This is **not X's official Trending Topics** list (not X Trending Topics rankings).

A read-only official X API is optional for people who already have permitted public search access. The skill never performs browser login, collects passwords or cookies, runs scheduled data collection, or auto-posts.

### 4. Install and get started

The easiest option: open this repository in Claude Code. The skill is already under .claude/skills/social-content-engine/. Start a new session and call /social-content-engine.

To install across local projects on Mac / Linux:

~~~bash
git clone https://github.com/caelynmoss/social-content-engine.git
mkdir -p ~/.claude/skills
cp -R social-content-engine/.claude/skills/social-content-engine ~/.claude/skills/
~~~

On Windows, copy the same folder to %USERPROFILE%\.claude\skills\. Check that SKILL.md is present and restart Claude Code.

[English setup guide](docs/SETUP_EN.md) · [Security](docs/SECURITY.md) · [Contributing](CONTRIBUTING.md)

[MIT License](LICENSE)
