# Social Content Engine — 中文介绍

**账号定位 × 真实个人风格 × 深度观点 × 可选 Research × X 内容创作**

这是开源的 Claude Code 写作 Skill，目标不是制造更多流畅的空话，而是帮助你从一个短想法出发，找到真实信息增量、符合账号定位的判断，再用你自己的语气写成短推、Thread、长帖或完整 Article。

它支持：Account Profile / Voice Profile（含 Humanity Fingerprint）、短观点自动扩展、五种 Writing Modes、R0/R1/R2 Research、Information Gain Card、Evidence Ledger、Human Voice Editor，以及得到你许可后才可保存的私人 Editorial Memory。

**Writing Modes：** 专业分析、轻松交流、研究驱动、鲜明观点、实践笔记。**Research：** R0 不做额外广泛研究；R1 核实关键依据；R2 深度交叉验证。两者独立，你可以「轻松交流 + R2 + Article」。

```text
/social-content-engine
我只有一个短观点：[粘贴]
先找出 2–3 个真正不同的切入角度、背后的机制和需要核实的细节。
用轻松交流模式 + R1 Research，推荐一个最有价值的角度，
在可用工具范围内核实真实来源，再用我的语气写一篇 Article。
不要编造来源、数据、观点或亲身经历。
```

**每天 CT 热点仍是手动触发**：输入「今天 Crypto Twitter 有什么热点？」即可尝试检索 X 公开讨论；没有真实帖子来源，就如实说明，不把普通新闻充作 CT 热点。

**安装：** Claude Code 打开仓库，使用 `/social-content-engine`，或将 `.claude/skills/social-content-engine` 复制至个人 `~/.claude/skills/`（Windows 为 `%USERPROFILE%\.claude\skills\`）。私人档案需授权才保存，不进入公开仓库，Skill 不自动发推。

查看[完整中英双语 README](README.md)、[中文使用指南](docs/SETUP_ZH.md)、[V5 评估方法](docs/V5_EVALUATION.md)。
