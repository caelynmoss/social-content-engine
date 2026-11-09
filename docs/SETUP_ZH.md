# 中文安装与使用教程

## 一、先安装 Skill

推荐直接在 Claude Code 中打开本 GitHub 仓库：`caelynmoss/social-content-engine`。项目中的 Skill 位于 `.claude/skills/social-content-engine/SKILL.md`，新建 Claude Code 会话就能调用。

想在其他本地项目也使用，Mac/Linux 用户将整个 `.claude/skills/social-content-engine/` 文件夹复制到 `~/.claude/skills/social-content-engine/`。Windows 放到 `%USERPROFILE%\.claude\skills\social-content-engine\`。

**必须复制整个文件夹，不要只复制 SKILL.md。** 如果重启会话后找不到 Skill，检查有没有多嵌套一层目录。

## 二、第一次使用：蒸馏个人风格

准备 8–20 条**本人**历史推文（3–5 条也可先做初步版本），有参考作者则明确标注他们不是自己。

```text
/social-content-engine
这是我自己写的推文：[粘贴]
这是供参考的同行写作：[粘贴]
请分析我真正的写作语气、论证方法、观点偏好、行文节奏与雷区。
不要模仿其他人的独特措辞。生成一份可校准的 Voice Profile。
先写一个样例让我修改。未经我同意不要持久保存私人档案。
```

如果暂时没有历史样本，也可以直接开始写作；但 Skill 会如实标注当前只是临时风格。

## 三、日常写推文

```text
/social-content-engine
我的观点：一个 Agent 能参与内盘，跟它自己作为发行方，是两个不同层级。
先帮我找逻辑漏洞和最值得写的独到角度，然后写一条英文短推。
不要替我捏造数据或把公司宣传硬塞进去。
```

也可以让它写完整 Thread、改写现有草稿、找反驳，或者通过一段语音转写整理想法。

## 四、手动运行 Crypto Twitter Radar

两种方式：

**官方 X API：** 需要你合法取得有公开 Recent Search 权限的 X API Bearer Token。将其放入自己的**私有运行环境的密钥配置**。不要把 Token、Cookie、X 密码放到 Chat、GitHub 或截图中。API 费用、额度由 X 决定。

从本仓库根目录执行：

```bash
python3 .claude/skills/social-content-engine/scripts/ct_radar.py collect \
  --topics examples/topics.example.json --max-queries 6 --per-topic 10 \
  --output data/private/ct-posts.json
python3 .claude/skills/social-content-engine/scripts/ct_radar.py rank \
  --input data/private/ct-posts.json \
  --output reports/private/radar.json --markdown reports/private/radar.md
```

**无 API：** 先手动提供 X 帖子的真实 ID、时间和正文（JSON），使用 `rank --input 你的文件`。提供的链接不能自动补全互动数，未知就保持未知。

Skill 返回的是**讨论信号**，不等于官方热搜。每条内容应该有原帖 URL、时间、讨论程度、可以追问的角度和风险。看到可能的新闻，还要验证事实和事件发生日期。

## 五、每天自动出一份 Radar

本 Skill **不会安装后自动开始运行**。如你能使用 Claude Code `/schedule` 云端定时任务，可以：

1. 先在云端定时任务的**私有运行环境**配置 `X_API_BEARER_TOKEN` 和访问 `api.x.com` 的网络权限。
2. 打开此 GitHub 仓库，让 Claude Code 根据 `routines/daily-radar.prompt.md` 创建一个每天运行的任务，例如「每天上午 10:00，时区 Asia/Kuala_Lumpur」。
3. 检查实际执行时间并手动试跑一次，确认报告包含可核实的 X 原帖。如果没有 Token，任务必须报告 `NOT_CONFIGURED`。
4. 报告保留在私人任务结果或 `.gitignore` 忽略的本地目录，**不要上传到 Public GitHub**。

注意：你在浏览器里登录过 X，不意味着 Claude Code 云端定时任务能接管这个登录状态。本项目不自动登录 X、读取 Cookie 或用脚本抓取网站。官方 API 的公开搜索也**不是**你的 Following 私人时间线。

## 六、遇到问题怎么排查

| 问题 | 处理方法 |
|---|---|
| 找不到 Skill | 确认整个目录、SKILL.md 路径正确，重新打开会话 |
| 提示没有 API Token | 在当前执行环境的私有配置里设置 X_API_BEARER_TOKEN |
| HTTP 401 / 403 | 检查 Token 权限和 recent search 访问资格 |
| HTTP 402 | 检查 X 开发者平台额度和账单 |
| HTTP 429 | 降低查询量，遵守 API 限速，不绕过限制 |
| 没找到足够热点 | 放宽搜索范围或如实输出少量讨论，不补造热点 |
| 云端任务看不到本地 Token | 云端与本地是不同运行环境，单独配置云端权限 |
| 写作不够像本人 | 提供自己更多真实内容，并用最终修改版校准 Voice Profile |

## 七、隐私与开源边界

大家可以使用同一份开源 Skill，但每个人都应保留独立的私人 Voice Profile。不要提交个人账号数据、X 抓取导出、真实用户样本、密钥或团队内部资料到公开仓库。任何推文都需本人检查，Skill 永远不自动发布。
