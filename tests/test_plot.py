import unittest
from gitsome.plot import plot_repo_by_commit_count, plot_repo_commit_history
import os

TEST_DIRECTORY = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
TEST_REPOS = [os.path.join(TEST_DIRECTORY, child) for child in os.listdir(TEST_DIRECTORY)]
print(TEST_REPOS)

class TestPlot(unittest.TestCase):
    def test_git_data(self):
        plot_repo_by_commit_count(TEST_REPOS).show()

    def test_plot_by_commit_history(self):
        plot_repo_commit_history(TEST_REPOS).show()
