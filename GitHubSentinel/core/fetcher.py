from utils.github_api import GitHubAPI

class UpdateFetcher:
    def __init__(self, config):
        self.config = config
        self.github_api = GitHubAPI(self.config["github_token"])
        self.last_check = {}

    def fetch_updates(self, repos):
        updates = {}
        for repo in repos:
            last_time = self.last_check.get(repo, None)
            new_updates = self.github_api.get_repo_updates(repo, since=last_time)
            if new_updates:
                updates[repo] = new_updates
                self.last_check[repo] = self.get_current_time()
        return updates
    
    def get_current_time(self):
        # 获取当前时间（待实现）
        pass
