# Social Content Engine — 中文说明

[返回中英双语 README](README.md) · [详细使用指南](docs/SETUP_ZH.md)

## 中文

**从一个简单想法，到真正有自己风格的 X 内容。**

Social Content Engine 是一款免费开源的 Claude Code Skill，包含三个核心能力：**个人风格蒸馏、观点思考与内容创作、按需 Crypto Twitter 热点研究**。不只是把一句话润色得更漂亮，而是帮助你找到值得表达的观点、理清论证，再用自己的语言写出来。

### 0. Account Alignment｜先有账号定位，再有单条内容的角度

**内容从账号定位开始，不从格式模板开始。** Account Profile 是一个账号的编辑章程，记录它面向谁、提供什么独特价值、核心观点、确认的立场、词汇偏好和不能碰的红线；Voice Profile 才负责这个作者如何表达。两份档案分别维护。

**Account Profile 第一行先回答：这个账号什么格式赢？** 使用账号自己的历史数据比较 Article、Long Post、Short Post、Thread，明确统计区间、样本量、指标和中位数。不同账号、不同内容类别可以有不同答案。证据不足就写 UNKNOWN / TEST NEEDED，不默认短推或 Thread。Article 是完整长文章格式，有标题、章节和论证，不等于把一条推文拉长；发布需确认账号权限。

企业或项目账号可通过独立的 approved-source register 指向获准公开的官方资料、核验日期、负责人和适用范围。没有经过批准的来源就不声称功能、合作、数据和时间已经确认。私人账号档案和来源文件不会自动上传到这个 Public 仓库。

如果用户同时管理个人号和官方号，可按需设置内容源头：**原创判断与真实故事从个人号首发，官方号注明来源并展开；教程、产品数据、合作和公告由官方号首发，个人号只在有新的独立观点时跟进**。这是可配置的建议，不是强制所有人都拥有两个账号。

~~~text
/social-content-engine
先帮我做 Account Alignment：明确账号受众、核心视角、词汇、立场和红线。
参考我授权提供的历史内容表现，先判断什么格式在这个账号有效。
这里是获准使用的官方事实来源：[URL 或私有文件路径]
如果有个人号和官方号，也帮我定义原创内容和引用的流向。
样本不足请标明，不要替我编造定位、指标或已批准事实。
~~~

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
| **Article（文章）** | 完整的 X 长文章：独立标题、章节结构、深入论证、案例与来源；适合研究、行业分析和系统性观点 |
| Long Post（长帖） | 一条较长的 X 帖子，承载完整观点，但不采用独立 Article 的文章结构 |
| Short Post（短推） | 单条简洁观察或判断 |
| Thread（推文串） | 多条推文逐步推进同一个论证，每条都有新内容 |
| Rewrite（改写） | 保留原意，把现有草稿改得更像本人 |
| Angle Exploration（角度探索） | 先找出不同角度、检验观点，再决定写什么 |

**一句话变短推：**

~~~text
/social-content-engine
我的想法：很多 AI Agent 仍然只是执行人的指令，
但这不等于真正的经济自主权。

帮我找到最有意思的切入角度，指出逻辑上的薄弱处，
再按我的个人风格写成一条英文短推。
不要营销腔，也不要替我编造事实。
~~~

**写一篇完整 Article：**

~~~text
/social-content-engine
我想写一篇英文 X Article，主题是：[你的观点 / 研究方向]。
先根据我的 Account Profile、历史格式表现与目标受众，确认 Article 是否适合这次内容。
使用我的 Voice Profile 来写，而不是套用通用营销文章格式。

请先帮我明确核心论点、找出证据不足的地方、提出可能的反驳，
再写出完整的文章：有标题、自然的章节结构、深入分析、必要的案例和来源，
以及真正推进观点的结尾。不要为了凑字数重复论述。

不要把 Article 强行压缩为 Long Post 或 Thread，也不要默认 300–1200 字符。
涉及产品数据或合作事实时，只使用我账号 approved-source register 中确认过的资料。
~~~

**Article、Long Post、Thread 是三种不同形式。** 选择哪一种，要看账号本身的历史表现、这次内容的目标和论证深度。**Article 没有统一的默认字数限制**；篇幅由账号实际数据和内容需求决定。正式发布前，请确认账号具有对应的 X Article 权限。

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

