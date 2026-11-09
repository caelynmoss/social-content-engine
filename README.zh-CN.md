# Social Content Engine — 中文使用说明

[返回中英双语 README](README.md) · [详细使用指南](docs/SETUP_ZH.md)

## 中文

**每天想看 Crypto Twitter 热点？直接问。** Social Content Engine 是免费开源的 Claude Code Skill：研究当天真实发生的 CT 讨论，帮你深挖个人观点，再写成短推、长推或 Thread。

**不需要定时任务，也不会自动运行。** 用户每次主动提问时，Skill 优先尝试当前环境可用的实时网页/X 搜索；已有官方 X API 权限时可选择扩大采样，但不是查询的前置条件。

### 能做什么？

- **今日 CT 热点：** 查找 BTC、ETH、DeFi、稳定币、Memecoin、AI x Crypto、安全事件、链上数据与相关政策在 X 上真实发生的讨论。
- **有证据的报告：** 5–10 个热点（不足就少给），包含 X 原帖链接、发布时间、讨论依据、哪些内容仍需核实、为什么值得关注和原创写作角度。
- **个人风格蒸馏：** 根据你自己的推文学习表达语气和论证习惯；同行作者只能提供写作技巧参考。
- **短推与 Thread：** 从一句话观点开始，先找逻辑漏洞和独特角度，再写成你的风格。

### 安装

在 Claude Code 打开本仓库，开始新会话即可。Skill 在 `.claude/skills/social-content-engine/`。如果要用于其他本地项目，可运行：

```bash
git clone https://github.com/caelynmoss/social-content-engine.git
mkdir -p ~/.claude/skills
cp -R social-content-engine/.claude/skills/social-content-engine ~/.claude/skills/
```

### 每天直接问

```text
/social-content-engine
今天 Crypto Twitter 有什么热点？
只要 CT 上真实有人讨论的 Crypto 话题，给我 5–10 个重点。
每个要有 X 原帖链接、发布时间、讨论依据、事实核查和可写的原创角度。
```

随后可以继续问：

```text
从第 2 个热点里选一个最有意思的角度，帮我写一条英文短推，
不要照抄原帖，保留我的语气。
```

**关于来源：** 公开搜索未必能覆盖所有 X 帖子。没有可核实的当日 X 原帖时，Skill 会如实说明，而不是拿普通新闻代替今天 CT 正在讨论的内容。“热点”指采样到的讨论信号，并非 X 官方 Trending Topics 排名。

可选的 X 官方 API 采集命令见 [中文使用指南](docs/SETUP_ZH.md)，不会自动启动、自动登录或发推。

