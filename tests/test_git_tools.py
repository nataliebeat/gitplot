import unittest
<<<<<<< HEAD:tests/test_main.py
from gitsome.main import find_repositories, get_commits, main, commit_is_since
=======
from app.git_tools import find_repositories, get_commits, scan_repos, commit_is_since
>>>>>>> 8bbf8a7 (move previous 'main' to 'git_tools'):tests/test_git_tools.py
from git import Repo, Commit
from datetime import timedelta, datetime, timezone
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
            all_since_last_week = get_commits(repo,commits=100)
            for commit in one_each:
                
               print(str(commit.message) + " one each")

            for commit in all_since_last_week:
                
                print(commit.committed_datetime)
                #print(str(commit.message) + " since last week")

    def test_commit_is_since(self):
        mock_late_commit = Mock()
        mock_late_commit.committed_datetime = datetime.now(timezone.utc) - timedelta(days=8)
        mock_early_commit = Mock()
        mock_early_commit.committed_datetime = datetime.now(timezone.utc) - timedelta(days=4)
        self.assertTrue(commit_is_since(mock_early_commit, timedelta(days=7)))
        self.assertFalse(commit_is_since(mock_late_commit, timedelta(days=7)))
        
    
    def test_scan_repos(self):
        print(scan_repos())
        

            
