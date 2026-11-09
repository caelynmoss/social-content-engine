# Social Content Engine

**个人 X 写作伙伴 + Crypto Twitter 热点研究 | Your personal X writing partner + Crypto Twitter radar**

[中文](#中文) · [English](#english)

---

## 中文

**把一个想法，写成真正像你自己的 X 内容。**

Social Content Engine 是一个免费开源的 Claude Code Skill。它能帮你分析个人写作风格、深入思考一个观点、生成短推或 Thread，还可以研究 Crypto Twitter（CT）上值得关注的讨论。

它不是简单的「AI 润色器」，也不是自动发推机器人。**任何主题都能写，内容由你审核并发布。**

### 它能做什么？

- **了解你的写作风格：** 从你自己写过的推文和反馈中学习语气、句式、论证习惯，以及你不喜欢的表达。
- **帮你把观点想透：** 从一句简单的想法开始，寻找更好的切入角度、反驳和证据，而不是替你编造观点。
- **写短推、长推和 Thread：** 支持中文和英文；也可以修改你已有的草稿。
- **发现 CT 热点：** 从 X 官方 API 的近期公开帖子中筛选有价值的讨论，保留原帖链接和时间；也可以手动提供帖子数据。

### 1. 安装

最简单的方式是：用 Claude Code 打开这个 GitHub 仓库，开始一个新会话。Skill 已放在 .claude/skills/social-content-engine/ 文件夹内。

如果你想在自己的其他本地项目里使用，Mac / Linux 可以运行：

~~~bash
git clone https://github.com/caelynmoss/social-content-engine.git
mkdir -p ~/.claude/skills
cp -R social-content-engine/.claude/skills/social-content-engine ~/.claude/skills/
~~~

Windows 用户可以手动复制整个文件夹到 %USERPROFILE%\.claude\skills\。请确保文件夹里有 SKILL.md，然后重新打开 Claude Code。

[查看详细中文安装教程](docs/SETUP_ZH.md)

### 2. 第一次使用：建立自己的 Voice Profile

最好先准备 8–20 条**自己写过**的推文或文章。参考作者可以提供，但要单独标注，Skill 不会直接复制他们的文案。

~~~text
/social-content-engine
这是我自己写的推文：[粘贴]
这是我喜欢的参考作者：[可选]
请分析我的写作风格、观点表达、句式和偏好，建立 Voice Profile。
再根据我的一个想法写条短推，让我确认像不像自己。
~~~

没有样本也能立即开始写，但一开始只能使用临时风格。个人档案只有经你允许才会保存到私人位置。

### 3. 平时怎么写？

~~~text
/social-content-engine
我的想法：很多 AI Agent 仍然只是执行人的指令。
先帮我检验这个观点，再写成一条自然的英文短推。
不要强行加入热点或编造事实。
~~~

你也可以要求「帮我写 5 条 Thread」「给我 3 个更好的角度」「改得更像我」。

### 4. 每日 Crypto Twitter 热点（可选）

~~~text
/social-content-engine
帮我分析最近 24 小时 Crypto Twitter 上值得关注的讨论。
重点关注 AI x Crypto、DeFi 和 Meme。
给出原帖链接、发布时间、讨论价值及可能的写作角度。
~~~

**自动读取真实 X 帖子需要自行配置具有公开搜索权限的 X API Bearer Token**。这不是用密码登录 X，也无法读取私人 Following 时间线。没有 API 权限时，可以手动提供帖子数据。

如果想每天自动生成报告，先完成 API 配置并验证采集成功，再按照 [中文设置教程](docs/SETUP_ZH.md) 和 [每日任务提示词](routines/daily-radar.prompt.md) 创建定时任务。安装 Skill **不会自动启动**任务。

> Radar 展示的是近期帖子里的「讨论信号」，不是 X 官方热搜榜。热门帖子不一定真实，写作前仍要核实。

### 更多信息

[中文安装指南](docs/SETUP_ZH.md) · [安全说明](docs/SECURITY.md) · [参与贡献](CONTRIBUTING.md)

基于 [MIT License](LICENSE) 开源。

---

## English

**Turn a rough idea into an X post that actually sounds like you.**

Social Content Engine is a free, open-source Claude Code skill. It helps you develop a personal writing voice, think through an argument, draft short posts or threads, and discover worthwhile Crypto Twitter (CT) discussions.

It is more than an AI rewriter, and it is **not** an auto-posting bot. Write about anything; you review and publish the final content.

### What can it do?

- **Learn your voice:** use your authentic posts and feedback to understand tone, rhythm, reasoning, and things you prefer to avoid.
- **Think with you:** examine assumptions, counterarguments and evidence instead of inventing opinions for you.
- **Draft X content:** short posts, eligible long posts and threads in Chinese or English, or improve existing drafts.
- **Explore CT signals:** rank recent public X posts from the official API, with dates and source links; manually provided data also works.

### 1. Install

The easiest way: open this GitHub repository as a Claude Code project and start a new session. The skill is already in .claude/skills/social-content-engine/.

For use across local projects on Mac / Linux:

~~~bash
git clone https://github.com/caelynmoss/social-content-engine.git
mkdir -p ~/.claude/skills
cp -R social-content-engine/.claude/skills/social-content-engine ~/.claude/skills/
~~~

On Windows, copy the whole folder to %USERPROFILE%\.claude\skills\. Make sure SKILL.md is present, then restart Claude Code.

[Full English installation guide](docs/SETUP_EN.md)

### 2. Build your Voice Profile

Start with 8–20 posts **you actually wrote**. You can provide reference writers separately, but their distinctive writing will not be copied.

~~~text
/social-content-engine
Here are posts I wrote: [paste]
Here are reference writers I admire: [optional]
Analyze my tone, argument style, sentence rhythm and writing preferences.
Build my Voice Profile, then draft one calibration post based on my idea.
~~~

You can still write immediately without samples, using a provisional voice. Saving any personal profile requires your permission.

### 3. Write a post

~~~text
/social-content-engine
My thought: Many AI agents still only follow human instructions.
Challenge my reasoning first, then write one natural short English post in my voice.
Don't invent facts or force a trending hook.
~~~

You can also say "Turn this into a five-post thread", "Suggest three stronger angles", or "Rewrite it in my voice".

### 4. Daily Crypto Twitter radar (optional)

~~~text
/social-content-engine
Find meaningful Crypto Twitter discussions from the past 24 hours.
Focus on AI x Crypto, DeFi and memes. Include original post links and dates,
why each is interesting and possible angles for an original post.
~~~

**Automated collection of real X posts requires a separately configured X API Bearer Token with permission to search public posts.** This is not a browser login and does not access your private Following feed. You can also provide your own source data.

To receive a daily report, configure and test API access first, then follow the [English setup guide](docs/SETUP_EN.md) and [daily task prompt](routines/daily-radar.prompt.md) to create a schedule. **Installation alone schedules nothing.**

> The radar shows sampled discussion signals, **not** official X Trending Topics. Verify claims before writing or posting.

### More

[English setup](docs/SETUP_EN.md) · [Security](docs/SECURITY.md) · [Contributing](CONTRIBUTING.md)

Open source under the [MIT License](LICENSE).
