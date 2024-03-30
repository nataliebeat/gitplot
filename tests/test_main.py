import unittest
from app.main import find_repositories, get_commits, main
from git import Repo, Commit

class TestGitSome(unittest.TestCase):
    def test_can_find_repos(self):
        repositories = find_repositories()
        print(repositories)
        for repository in repositories:
            self.assertIsInstance(repository, Repo)
            commits = get_commits(repository)
            for commit in commits:
                self.assertIsInstance(commit, Commit)

        main() 
    
