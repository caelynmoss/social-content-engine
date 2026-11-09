# 中文安装与使用指南

## 一、安装 Skill

Claude Code 中直接打开本仓库，Skill 位于 `.claude/skills/social-content-engine/SKILL.md`。也可以将整个 `social-content-engine` 文件夹复制到个人 `~/.claude/skills/` 目录（Windows：`%USERPROFILE%\.claude\skills\`），然后重开 Claude Code 会话。

## 二、每天按需查询 CT 热点

```text
/social-content-engine
今天 Crypto Twitter 有什么热点？
请只分析今天 CT 上真正讨论的 Crypto 话题，给出 5–10 个重点。
每条要有 X 原帖链接、原帖时间、不同账号的讨论依据、
为什么重要、消息是否核实、我能写的独立角度。
```

只要**当天自己输入一次**即可，完全不需要自动启动、后台运行或定时配置。Skill 会首先尝试现有的合法实时搜索工具。若无法访问可验证的 X 原帖，它会如实说明，不会用普通新闻冒充 CT 热点。

“今天”指用户当地时间从 00:00 到查询时刻；“过去 24 小时”是滚动窗口。Skill 应显示使用的日期、时区、截止时间。多个独立 X 作者的发帖是比单一帖子更强的讨论证据。

## 三、将热点写成个人推文

```text
/social-content-engine
针对第 2 个热点，先帮我找论证漏洞和更特别的角度，
然后根据我的风格写一条英文短推，不要复制其他人的句子。
```

可提供 8–20 条自己写过的推文，帮助建立 Voice Profile。没有历史内容也可以先用临时风格。个人档案的持久保存需要本人明确许可。

## 四、官方 X API（可选，仅手动使用）

已有公开 Recent Search 权限和额度时，可以把 `X_API_BEARER_TOKEN` 安全配置在自己的私有运行环境中，手动执行：

```bash
python3 .claude/skills/social-content-engine/scripts/ct_radar.py collect \
  --topics examples/topics.example.json --hours 24 --max-queries 6 --per-topic 10 \
  --output data/private/ct-posts.json
python3 .claude/skills/social-content-engine/scripts/ct_radar.py rank \
  --input data/private/ct-posts.json \
  --output reports/private/radar.json --markdown reports/private/radar.md
```

但**它不是普通 CT 热点查询的前置条件**，没有 API 也可通过当前实时搜索工具查找公开 X 帖子，或手动提供真实来源。测试用的虚构数据不能作为实时 CT 证据。

## 五、注意事项

无法验证原帖就要说明，不填充虚构热点；X 官方 API 可能涉及费用、限速和权限。绝不索取 X 密码、Cookie，不执行自动网页登录、定时任务、自动发推或其他账号操作。请将个人 Voice Profile、API 密钥和 X 原始数据保存在私人空间。
