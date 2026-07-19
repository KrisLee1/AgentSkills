# 贡献指南

[English](CONTRIBUTING.md)

感谢你帮助改进 AgentSkills。

请先阅读[开发指南](docs/DEVELOPMENT.zh-CN.md)，了解仓库结构、skill 编写约定和验证命令。

## 新增或修改 skill

1. 每个 skill 必须自包含在 `skills/<skill-name>/` 目录中。
2. 必须提供 `SKILL.md`，其 front matter 中包含唯一的 `name` 和清晰的 `description`。
3. 指令应聚焦、具体，并严格限定在该 skill 的职责范围内。
4. 将可复用模板放在 `assets/`，参考资料放在 `references/`，可执行辅助工具放在 `scripts/`。
5. 当行为、输出、要求或随附资源发生变化时，新增或更新该 skill 面向用户的 `README.md` 和 `README.zh-CN.md`。
6. 不要加入个人数据、凭据或机器相关的绝对路径。

## 提交拉取请求前

- 运行[开发指南](docs/DEVELOPMENT.zh-CN.md)中记录的 Markdown 和脚本检查。
- 确保脚本默认安全，未经明确确认不会覆盖用户文件。
- 新增、重命名或删除 skill 时，同步更新根 README 和使用指南的中英文版本。
- 在拉取请求中说明要解决的问题和预期行为。

## 行为准则

在所有项目讨论中保持尊重、建设性和体谅。
