import unittest
from core.subscription import SubscriptionManager

class TestCore(unittest.TestCase):
    def test_subscription_manager(self):
        config = {"subscriptions": ["test/repo"]}
        manager = SubscriptionManager(config)
        self.assertEqual(manager.get_repos(), ["test/repo"])

if __name__ == "__main__":
    unittest.main()
