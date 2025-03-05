import requests

class GitHubAPI:
    def __init__(self, token):
        self.token = token
        self.headers = {"Authorization": f"token {token}"}

    def get_repo_updates(self, repo, since=None):
        # 获取仓库更新（Commits、Issues、PRs 等）
        url = f"https://api.github.com/repos/{repo}/events"
        params = {"since": since} if since else {}
        response = requests.get(url, headers=self.headers, params=params)
        return response.json()

    def get_repo_stats(self, repo, period="week"):
        # 获取仓库统计数据
        pass
