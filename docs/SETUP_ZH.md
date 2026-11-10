# 中文安装与使用指南 — V5

## 1. 安装

在 Claude Code 打开本仓库：`.claude/skills/social-content-engine/SKILL.md` 已存在。或将整个 `social-content-engine` Skill 文件夹复制到 `~/.claude/skills/social-content-engine/`（Windows：`%USERPROFILE%\.claude\skills\social-content-engine\`），重新打开会话后输入 `/social-content-engine`。

## 2. 建立账号与个人风格（可选但建议）

Account Profile 决定账号定位、受众、词汇、立场、红线、批准的官方事实来源和什么格式真正有效；Voice Profile 决定作者怎样表达。提供自己写过的 8–20 条文章/推文、账号内容表现（如有）与修改反馈。没有充分数据时将有效格式标为 UNKNOWN，不默认短推。Article 是完整长文章，而不是 Long Post 或 Thread。所有私有档案只有明确授权才保存。

## 3. 从一句话开始写深

```text
/social-content-engine
我的观点是：[粘贴一两句话]。
先用 Idea Expansion 找 2–3 个真正不同的机制、后果、反例和证据空缺，
不要把原句机械扩写。推荐一个方向，同时给我一份初步草稿。
```

如果明确只要成稿，Skill 应直接交付，不强制先选模式。若你想选择，五种表达方式分别是：PROFESSIONAL（专业分析）、CONVERSATIONAL（轻松交流）、RESEARCH_DRIVEN（研究驱动）、OPINIONATED（鲜明观点）、BUILDERS_NOTES（实践笔记）。选择只作用于当前稿件，不修改私人档案。

## 4. Research 可独立选择

- R0：基于你的素材推理，不做额外广泛研究，但重要事实仍要核实或限定。
- R1：在可用、授权的研究工具下，尝试核实 1–3 项最有价值的证据。
- R2：深度查证原始资料、时间、对立证据、数据口径和重要机制。

Research 深度、表达方式和 Article/Long Post/Short Post/Thread 格式是三个独立选择。例如：「CONVERSATIONAL + R2 + ARTICLE」。Research 能否执行取决于当次 Claude Code 工具、访问权限和源数据。不能访问时，Skill 必须说明并保持事实表述谨慎；不得伪造论文、统计或来源链接。

## 5. 信息差和 Evidence Ledger

要求：`帮我找一个足以改变读者判断、CT 上不一定被讨论清楚的具体事实或机制。先找原始资料，把已经证实、来源声称、尚未证实和作者推论分开，再给出原创角度。` 只有实际采样 X 讨论，才可断言「CT 没人注意」。Skill 会使用 `references/information-gain.md` 的 Information Gain Card。Article 可用多个有证据的卡片深化论点，而非凑字数。

## 6. 写得更像本人 + Editorial Memory

`这个输出不太像我：请诊断是观点浅、缺乏细节、证据不足还是表达不自然，再按我的历史最终稿调整；不要自己编故事。` 若你提供最终修改稿，Skill 可以提出一条可检验的长期编辑偏好（PROPOSED）；**未经你明确同意，不得保存到私人 Editorial Memory**，更不得写入 GitHub。

## 7. CT Radar（手动查询）

`/social-content-engine 今天 CT 上真正讨论的 Crypto 热点有哪些？请提供可核实的原帖链接、时间和讨论依据。` 只在询问时研究，不自动运行。可选使用已授权的 X 公开搜索 API，或当前可用的合法实时检索；若不能验证 X 原帖，不用新闻网站凑热点。

## 8. 安全与真实性

永不自动发推、回复、转发、关注或登录 X，不收集密码与 Cookie。个人文章、数据、来源批准表和密钥不进入公开仓库。使用 X API 时自行核对费用和授权。未经核实的数据不得被写成事实。详见 `docs/SECURITY.md`。
