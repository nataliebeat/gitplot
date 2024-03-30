import unittest
from app.main import find_repositories, get_commits, main
from git import Repo, Commit
from datetime import timedelta

class TestGitSome(unittest.TestCase):
    def setUp(self):
        self.repos = find_repositories()
    def test_can_find_repos(self):
        for repo in self.repos:
            self.assertIsInstance(repo, Repo)

    def test_can_get_commits(self):
        for repo in self.repos:
            one_each = get_commits(repo)
            all_since_last_month = get_commits(repo,commits=100, since=timedelta(weeks=1))
    def test_main(self):
        main()

            
