import unittest
from app.plot import git_data, plot_repo_by_commit_count

class TestPlot(unittest.TestCase):
    def test_git_data(self):
        plot_repo_by_commit_count()
