# Your AI Writing Partner — 中文使用说明

[中英双语 README](README.md) · [中文安装指南](docs/SETUP_ZH.md)

## 中文

**一个粗糙的想法，也值得写成有自己观点、有新信息、有人味的内容。**

Your AI Writing Partner 是一个免费开源的 Claude Code Skill。你可以给它一句想法、几条笔记、一篇草稿，或一个想研究的话题。它会帮助你**理清观点 → 挖掘角度和信息差 → 按需核查证据 → 用自己的语气创作**，而不是只把原句写长、写漂亮。

适合个人创作者、研究者、Builder，也能用于有明确定位和事实审批要求的官方账号。**写作主题不限于 Crypto；只有 CT Radar 专门关注 Crypto Twitter。**

### 先开始：安装与第一条内容

**方式 A：直接在项目里使用。** 用 Claude Code 打开这个仓库，Skill 已放在 .claude/skills/social-content-engine/；开启新会话后使用 /social-content-engine。

**方式 B：安装到个人目录，在其他项目也能使用。** Mac / Linux：

~~~bash
git clone https://github.com/caelynmoss/social-content-engine.git
mkdir -p ~/.claude/skills
cp -R social-content-engine/.claude/skills/social-content-engine ~/.claude/skills/
~~~

Windows：将整个 .claude/skills/social-content-engine 文件夹复制到 %USERPROFILE%\.claude\skills\，确认里面有 SKILL.md，再重开 Claude Code。

**不用先建立档案也能开始：**

~~~text
/social-content-engine

我有一个想法：AI Agent 能使用钱包，不代表它真正拥有经济自主权。

先帮我找到三个有实质区别的切入角度，
推荐其中最有价值的一个，指出缺少什么事实或证据，
然后写成一条自然、有信息量的英文 X 帖子。
不要编造经历、数字或引用。
~~~

Skill 会提供候选思路，但**不会擅自认定那些新观点就是你本人的立场**。如果你只想直接要成稿，也可以说「不要解释，直接写一版」。

### 它能解决哪些问题？

| 你的问题 | 对应能力 | 你会得到什么 |
| --- | --- | --- |
| 写出来很像 AI，不像我 | **Voice Distillation + Human Voice Editor** | 基于你真实写作和修改习惯的表达方式，而不是强行加口语词 |
| 只有一句很笼统的观点 | **Adaptive Idea Expansion** | 2–3 个不同的机制、影响、反例与可验证方向 |
| 内容正确但没有干货 | **Information Gap Mining** | 可能改变读者判断的具体事实/机制和待核实的问题 |
| 我想加权威研究 | **R0 / R1 / R2 Research** | 按需查证，并区分已核实事实、来源声称与推论 |
| 这次想专业或轻松一点 | **Writing Mode** | 让这一篇内容改变表达方式，同时保留个人风格 |
| 不知道写 Article 还是 Thread | **Account Profile + Format Evidence** | 根据你这个账号自己的表现和内容目标决定 |
| 今天 CT 在讨论什么 | **On-demand CT Radar** | 有真实 X 原帖和发布时间的 Crypto 讨论线索 |

### 1. 先定义账号，再学你的表达

**Account Profile** 记录账号定位、受众、内容方向、认可的立场、常用词和红线。第一行优先回答：**「什么格式在我这个账号真正有效？」** 依据真实历史数据判断；没有数据就标记 UNKNOWN，不会默认短帖或 Thread。涉及公司或产品事实时，还可以设置私有的 **approved-source register**。

**Voice Profile** 则从你自己写过的 **8–20 条推文或 Article** 和你对 AI 草稿的真实修改中，提炼句式、节奏、思考习惯、幽默感、表达不确定性的方式，以及你经常删除的 AI 套话。这部分也叫 **Humanity Fingerprint**。参考作者只用于学习通用技巧，不会模仿他们独有的表达。

~~~text
/social-content-engine

这些是我自己最终发出的 10 条内容：[粘贴]
这些是我改过的 AI 草稿与最终稿：[可选]
请先分析 Account Profile 和 Voice Profile；
提炼我的 Humanity Fingerprint，并写一条校准样本。
告诉我哪些特征有样本支持，哪些只是暂时推测。
~~~

### 2. 短观点也能写深：Idea Expansion

例如只输入「AI Agent 还不够自主」，Skill 不应该只生成一句「真正的自主不是执行，而是决策」。它会先提出可能的不同问题：

- **权限归属：** 谁能修改规则、停止执行或撤回资产控制？
- **责任分配：** 出错后风险由谁承担，谁有纠错权限？
- **经济激励：** 谁真正控制收益、流动性与运营决策？

以上只是**示范性的研究方向，不是已经核实的现实结论**。Skill 会找到可以验证的细节，区分作者观点、AI 建议和研究事实；如果某个角度缺乏证据，会保留疑问，而不是写得像已经证实。

### 3. 选择表达方式：五种 Writing Modes

Writing Mode 决定**这一篇怎么说**，不会更改你的长期人格或账号定位。

| Writing Mode | 表达感觉 | 比较适合 |
| --- | --- | --- |
| **Professional** | 专业、清晰、克制 | 行业判断、正式分析 |
| **Conversational** | 轻松、自然、像真实交流 | 个人观察、讨论 |
| **Research-Driven** | 研究方法清楚、证据扎实 | Article、市场分析 |
| **Opinionated** | 立场鲜明，兼顾反驳 | 个人观点、QRT |
| **Builder's Notes** | 从真实操作、限制和复盘出发 | Build in Public、工作经验 |

你可以主动指定，也可以让 Skill 根据账号与写作目标**推荐一个合适的默认模式**。不用每次做选择题；明确说「直接写」就直接写。

### 4. Research 是独立开关，不等于写作语气

| 深度 | 实际含义 |
| --- | --- |
| **R0 · Original Thinking** | 基于现有想法推理，不额外做广泛研究；重要事实仍须核实或限定 |
| **R1 · Evidence Supported** | 尝试找到 1–3 条最相关的真实证据，既可能支持也可能挑战你的观点 |
| **R2 · Deep Research** | 深入查找一手材料、数据口径、反证、背景与具体机制，并交叉检查 |

例如 **Conversational + R2 + Article** 是完全可行的：文章读起来很自然，背后的研究仍然严谨。

**Information Gap Mining** 专门寻找那些*具体而重要*、但常被泛泛叙事掩盖的细节：链上权限、资金和激励归属、真实使用数据、机制约束、历史变化等。找到材料后，Skill 用 **Information Gain Card** 说明「发现了什么、来源是什么、为何影响判断」，并用 **Evidence Ledger** 区分：

- **Verified evidence：** 已实际核查、支持特定范围结论的证据。
- **Source claim / Disputed：** 来源自己的说法，或仍有争议的信息。
- **Unverified / Suggested hypothesis：** 尚待核实的内容或供你选择的推论。

**重要：** Skill 只能使用当前环境真正能访问的来源。没查到就说没查到，不能杜撰论文、数据或 X 原帖。只有实地采样到相关 CT 讨论，才可以判断一个角度在所采样的 CT 内容中是否较少被提及。

### 5. 内容形式：Article 是正式格式

| 格式 | 用途 |
| --- | --- |
| **Article** | 完整长文章：标题、章节、论证、案例、数据、来源与结论 |
| **Long Post** | 单条较长的 X 帖子，围绕一个完整观点展开 |
| **Short Post** | 一条简洁的观察或判断 |
| **Thread** | 多条推文逐步推进同一论证 |

长度与格式依赖**账号自己的表现、主题深度及你的要求**，不采用统一字符数模板。Article 不会被强行缩成 Thread 或 Long Post；X 原生 Article 发布权限需要另行确认。

**组合示例：从一句话到有研究支撑的 Article**

~~~text
/social-content-engine

主题：AI Agent 还没有真正的经济自主权。
Format：ARTICLE
Writing Mode：CONVERSATIONAL
Research：R2

先提出 2–3 个真正不同的潜在角度，分析机制、反例和证据缺口。
请从可访问的原始研究、技术文档、链上资料中查证，
尝试找 2 个能改变读者判断的 Information Gain。
先告诉我哪些发现已核实，哪些仍只是来源声明或假设。

然后选一个最有内容的角度，参考我的 Account Profile 和 Voice Profile，
写一篇自然、扎实的中文 Article。不要模仿任何参考作者，
也不要把我没说过的话或没做过的事情写成我的经历。
~~~

### 6. 内容还是太像 AI？让它从你的修改中学

~~~text
/social-content-engine

这是 Skill 写的草稿：[粘贴]
这是我自己改完的版本：[粘贴]

请比较两版，找到真正造成“AI 味”的问题：
是角度空泛、细节不足、证据薄弱，还是语言节奏不像我？
先把当前稿件改好，再提出一条可检验的 Editorial Memory 规则。
只有我明确同意才保存这条长期偏好。
~~~

**Editorial Memory** 保存的是经过你确认的编辑习惯，而不是自称已经「理解你的性格」。个人样本、Voice Profile、账号档案和研究资料都应保留在你的私人空间，**不会自动写入公开 GitHub 仓库**。

### 7. 每天的 Crypto Twitter 热点：手动问一次

~~~text
/social-content-engine

今天 Crypto Twitter 上真实发生了哪些值得关注的讨论？
只要 Crypto 相关的 CT 话题，给我最多 5–10 个有证据的主题。
附真实 X 原帖链接、发布时间、主要分歧、
消息是否已核实，以及值得进一步调查的信息差。
~~~

CT Radar **仅在你主动请求时运行**，不会自动登录 X、定时采集或发推。它需要当前环境可用的合法实时搜索，或可选、已获授权的官方 X API。新闻网站可以帮助核实事实，但**不能替代 X 原帖证明「CT 正在讨论」**。结果是采样的讨论信号，**不是 X Trending Topics 官方榜单**；若来源不足，会坦诚减少条目。

### 适用边界与更多文档

- **作者主权：** Skill 不替你决定立场、编造第一人称经历，也不强行加入品牌宣传。
- **官方账号：** 产品数据、合作与公告必须使用获准公开且仍适用的资料；个人号与官方号可设置不同的内容首发规则。
- **安全：** 仅产出草稿；不自动发布、关注、转发、登录 X，不索取密码或 Cookie。
- **可信度：** R1/R2 表示研究要求，不代表外部来源一定可访问；不能把未经核实的材料写成已验证的事实。

[中文详细安装与使用](docs/SETUP_ZH.md) · [V5 质量评估方法](docs/V5_EVALUATION.md) · [安全与隐私](docs/SECURITY.md) · [参与贡献](CONTRIBUTING.md)

