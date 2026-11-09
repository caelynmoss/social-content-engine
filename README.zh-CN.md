# Social Content Engine — 中文使用说明

**一套同时支持个人风格蒸馏、观点深挖、X 推文写作与每日 Crypto Twitter 热点研究的 Claude Code Skill。**

[English README](README.md) · [详细中文安装指南](docs/SETUP_ZH.md) · [安全说明](docs/SECURITY.md)

## 它能做什么？

Social Content Engine 不负责替你批量制造营销文案，而是帮你把零散想法变成**自己真正认同、能站得住脚、符合个人语气**的内容。

- **个人风格蒸馏：** 通过本人写过的推文以及修改反馈，学习表达方式、思考习惯、行文节奏和内容偏好。同行作者只作为写作技巧参考，不照抄。
- **AI Thinking Partner：** 帮你发现有价值的切入点、挑战逻辑漏洞、寻找反证，再组织观点。
- **短推、长推、Thread：** 支持中文和英文，不限 AI Agent 或 Crypto 主题。
- **每日 CT Radar：** 可使用 X 官方 API 读取最近的公开推文，筛选几条值得研究的话题，并说明原帖、时间、讨论信号和可能的写作角度。
- **没有 API 也能使用：** 手动提供经过核实的 X 帖子或 JSON 数据，离线筛选；数据不足就如实说明。

**重要区别：** 我们选的是近期 Crypto Twitter 上值得注意的「讨论信号」，不等于 X 官方热搜，也不代表帖子里的消息已被证实。Skill 不会自动发推。

## 第一步：安装到 Claude Code

打开这个 GitHub 仓库作为 Claude Code 项目，Skill 已经放在 `.claude/skills/social-content-engine/`。

如果你想在所有本地项目中使用，可以把整个 `social-content-engine` 文件夹复制到：

- Mac / Linux：`~/.claude/skills/social-content-engine/`
- Windows：`%USERPROFILE%\.claude\skills\social-content-engine\`

最后应当能看到 `SKILL.md`，重新打开 Claude Code 的会话即可。

## 第二步：建立自己的 Voice Profile

准备 8–20 条自己写的推文（少量样本也能先做初步版本），可选 2–4 个参考创作者。输入：

```text
/social-content-engine
下面是我自己写过的推文；另一部分是我喜欢的同行参考文章，请严格区分两组。
帮我提炼自己常用的论证方式、语气、句式、选题品味以及讨厌的表达方式。
先形成一份 Voice Profile，再用我的一个观点写一条短推让我校准。
个人档案仅放在我的私人本地目录，不要提交到公共仓库。
```

## 第三步：每天写推文

```text
/social-content-engine
我有个想法：很多所谓 Agent 自治，实际上还是人类在替它决定最关键的事。
先帮我反驳和补全这个观点，然后按我的个人语气写一条英文短推。
不要为了显得有深度而添加我没说过的事实。
```

或者：

```text
/social-content-engine
给我 5 条真正有原帖来源的最近 24 小时 CT 讨论信号。
我对 AI x Crypto、Meme、加密市场结构更感兴趣。
从中选出最适合我写的 2 个角度，但不要替我预设立场。
```

## 第四步：配置自动每日热点研究（可选）

仅安装 Skill **不会自动采集**。要实现每天自动读取 X 的公开讨论，需要：

1. 有合法的 X 开发者 API 访问权限（取决于实际套餐、额度和费用）。
2. 在你自己的 Claude Code 定时任务执行环境里安全配置 `X_API_BEARER_TOKEN`；不要在聊天、截图或 GitHub 文件中粘贴密钥。
3. 使用 Claude Code `/schedule` 创建每日任务，采用 `routines/daily-radar.prompt.md` 提供的任务指令。核对时区与下次运行时间。
4. 首次先手动执行一次，验证数据来自真实的 X API 且带原帖链接。

**不能直接让云端 Claude Code 继承你在浏览器登录过的 X 账号。** 官方 API 的公开搜索并不是你的个人 Following 时间线。为了遵守 X 的自动化规则，本项目不会自动登录网页、读取 Cookie 或模拟浏览器无人值守抓取。没配置 API 时只能手动提供数据，不能伪造热点。

详细图文替代步骤、终端命令及问题排查请看：[docs/SETUP_ZH.md](docs/SETUP_ZH.md)。

## 团队怎么用？

大家可以安装同一个 Skill，但是**各自保存独立的 Voice Profile**。不要把团队成员的个人样本、声音档案、API Key 或采集数据上传到这个 Public GitHub 仓库。Skill 本身开源，不等于个人材料公开。

## 许可证

MIT License，见 [LICENSE](LICENSE)。
