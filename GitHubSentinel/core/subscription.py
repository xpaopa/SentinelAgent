class SubscriptionManager:
    def __init__(self, config):
        self.config = config
        self.repos = self.load_subscriptions()

    def load_subscriptions(self):
        # 从配置文件中加载订阅的仓库列表
        return self.config.get("subscriptions", [])

    def add_repo(self, repo_url):
        # 添加新的订阅仓库
        if repo_url not in self.repos:
            self.repos.append(repo_url)
            self.save_subscriptions()
    
    def remove_repo(self, repo_url):
        # 删除订阅仓库
        if repo_url in self.repos:
            self.repos.remove(repo_url)
            self.save_subscriptions()
    
    def save_subscriptions(self):
        # 保存订阅列表到配置文件
        self.config["subscriptions"] = self.repos
        # 实现保存逻辑（待细化）
    
    def get_repos(self):
        return self.repos
