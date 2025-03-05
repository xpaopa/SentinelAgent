import schedule
import time
from core.subscription import SubscriptionManager
from core.fetcher import UpdateFetcher
from core.notifier import Notifier
from core.reporter import Reporter
from utils.logger import Logger

class GitHubSentinel:
    def __init__(self, config_path="config/settings.yaml"):
        self.logger = Logger("github_sentinel")
        self.config = self.load_config(config_path)
        self.subscription = SubscriptionManager(self.config)
        self.fetcher = UpdateFetcher(self.config)
        self.notifier = Notifier(self.config)
        self.reporter = Reporter(self.config)
    
    def load_config(self, path):
        # 加载配置文件（待实现）
        pass
    
    def run(self):
        self.logger.info("Starting GitHub Sentinel...")
        self.schedule_tasks()
        while True:
            schedule.run_pending()
            time.sleep(60)  # 每分钟检查一次任务
    
    def schedule_tasks(self):
        # 每日检查更新
        schedule.every().day.at("08:00").do(self.check_updates)
        # 每周生成报告
        schedule.every().monday.at("09:00").do(self.generate_weekly_report)

    def check_updates(self):
        updates = self.fetcher.fetch_updates(self.subscription.get_repos())
        if updates:
            self.notifier.notify(updates)
    
    def generate_weekly_report(self):
        report = self.reporter.generate_report(self.subscription.get_repos())
        self.notifier.notify(report, type="report")

if __name__ == "__main__":
    sentinel = GitHubSentinel()
    sentinel.run()
