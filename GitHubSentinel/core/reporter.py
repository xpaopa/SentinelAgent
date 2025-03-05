from utils.github_api import GitHubAPI

class Reporter:
    def __init__(self, config):
        self.config = config
        self.github_api = GitHubAPI(self.config["github_token"])

    def generate_report(self, repos):
        report = {"repos": {}, "summary": {}}
        for repo in repos:
            stats = self.github_api.get_repo_stats(repo, period="week")
            report["repos"][repo] = stats
        report["summary"] = self.generate_summary(report["repos"])
        return report
    
    def generate_summary(self, repo_stats):
        # 生成报告总结（待实现）
        pass
