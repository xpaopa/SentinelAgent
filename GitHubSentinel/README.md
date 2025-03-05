# GitHub Sentinel

GitHub Sentinel 是一款开源的 AI 驱动工具，专为开发者和项目管理人员设计，用于自动化跟踪和管理 GitHub 仓库动态。它支持订阅管理、定期更新获取（每日/每周）、多渠道通知（邮件、Slack 等）以及报告生成，帮助团队高效协作，及时响应项目变更，确保始终掌握最新进展。

## 核心功能

- **订阅管理**：轻松添加或移除关注的 GitHub 仓库。
- **更新获取**：自动抓取仓库的最新动态（如 Commits、Issues、PRs）。
- **通知系统**：通过邮件、Slack 等渠道实时推送更新。
- **报告生成**：生成周期性项目进展报告，洞察团队工作情况。

## 使用场景

- **开发者**：快速了解依赖仓库的更新。
- **项目经理**：监控团队项目进展，提高管理效率。
- **开源贡献者**：跟踪感兴趣的项目动态。

## 技术栈

- **编程语言**：Python 3.8+
- **核心库**：
  - `requests`：与 GitHub API 交互。
  - `schedule`：实现定时任务。
  - `pyyaml`：解析配置文件。
- **通知支持**：
  - 邮件：基于 `smtplib`（计划集成）。
  - Slack：通过 Webhook API。
- **扩展性**：模块化设计，支持添加新功能（如数据库存储、CLI 界面）。

## 安装

1. 克隆仓库：
   ```bash
   git clone https://github.com/<your-username>/GitHubSentinel.git
   ```
2. 进入项目目录：
   ```bash
   cd GitHubSentinel
   ```
3. 安装依赖：
   ```bash
   pip install -r requirements.txt
   ```
4. 配置 `config/settings.yaml`（参考示例文件）。
5. 运行：
   ```bash
   python main.py
   ```

## 配置

编辑 `config/settings.yaml` 文件，设置 GitHub 令牌、订阅仓库和通知渠道。例如：

```yaml
github_token: "your_github_personal_access_token"
subscriptions:
  - "owner/repo1"
  - "owner/repo2"
notification_channels:
  - "email"
  - "slack"
email_settings:
  smtp_server: "smtp.example.com"
  smtp_port: 587
  sender: "sentinel@example.com"
  recipients:
    - "user1@example.com"
slack_webhook: "https://hooks.slack.com/services/xxx/yyy/zzz"
```

## 未来计划

- **数据库支持**：集成 SQLite 或 PostgreSQL，持久化存储订阅和更新历史。
- **CLI 界面**：添加命令行工具，方便管理订阅和查看报告。
- **更多通知渠道**：支持 Discord、Telegram 等。
- **智能分析**：引入 AI 分析更新内容，生成更具洞察力的报告。
- **Web 仪表盘**：开发一个简单的 Web UI，用于可视化管理和监控。

## 贡献

欢迎提交 Issues 或 Pull Requests，共同完善这个工具！请遵循以下步骤：

1. Fork 本仓库。
2. 创建特性分支：
   ```bash
   git checkout -b feature/new-feature
   ```
3. 提交更改：
   ```bash
   git commit -m "Add new feature"
   ```
4. 推送分支：
   ```bash
   git push origin feature/new-feature
   ```
5. 创建 Pull Request。

## 许可证

本项目采用 MIT 许可证。
