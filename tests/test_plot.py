import unittest
from gitsome.plot import git_data, plot_repo_by_commit_count, plot_repo_commit_history

class TestPlot(unittest.TestCase):
    def test_git_data(self):
        plot_repo_by_commit_count().show()

    def test_plot_by_commit_history(self):
        plot_repo_commit_history().show()
