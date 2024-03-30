import unittest
from app.main import find_repositories, get_commits 
from git import Repo

class TestGitSome(unittest.TestCase):
    def test_can_find_repos(self):
        repositories = find_repositories()
        print(repositories)
        for repository in repositories:
            self.assertIsInstance(repository, Repo)
            commits = get_commits(repository)
            print(commits)
    
