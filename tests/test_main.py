import unittest
from app.main import find_repositories, get_commits, main
from git import Repo, Commit
from datetime import timedelta
from unittest.mock import Mock, patch

class TestGitSome(unittest.TestCase):
    def setUp(self):
        self.repos = find_repositories()
    def test_can_find_repos(self):
        for repo in self.repos:
            self.assertIsInstance(repo, Repo)

    def test_can_get_commits(self):
        for repo in self.repos:
            one_each = get_commits(repo)
            all_since_last_week = get_commits(repo,commits=100, since=timedelta(weeks=1))
            for commit in one_each:
                
               print(str(commit.message) + " one each")

            for commit in all_since_last_week:
                
                print(commit.committed_datetime)
                print(str(commit.message) + " since last week")

    def test_commit_is_since(self):
       pass 

    @unittest.skip("funsies")
    def test_main(self):
        main()

            
