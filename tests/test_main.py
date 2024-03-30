import unittest
from app.main import find_repositories 
from git import Repo

class TestGitSome(unittest.TestCase):
    def test_can_find_repos(self):
        repositories = find_repositories()
        for repository in repositories:
            self.assertIsInstance(repository, Repo)
