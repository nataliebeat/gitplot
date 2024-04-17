"""Plots data from git directories using the .git_tools module and matplotlib"""

from datetime import datetime, timedelta
import matplotlib.pyplot as plt
from .git_tools import scan_repos, commit_is_since

def plot_repo_by_commit_count(repo_dirs):
    """Plots amount of commits of given git directories"""
    git_data = scan_repos(repo_dirs)
    repos = list(git_data.keys())
    repo_commits = git_data.values()
    commit_count = [len(commits) for commits in repo_commits]
    plt.figure(figsize=(9,4))
    plt.bar(repos, commit_count)
    return plt

def plot_repo_commit_history(repo_dirs, days: int = 70):
    """Plots commit histories of given git directories since 'days' argument"""
    git_data = scan_repos(repo_dirs, since=timedelta(days=days))
    repos = list(git_data.keys())
    today = datetime.now()
    dates = []
    for day in range(0, days):
        dates.append(today - timedelta(days=day))
    plt.figure()
    for repo in repos:
        commit_history = []
        for date in dates:
            date_since = today - date
            repo_commits = \
            [commit for commit in git_data[repo] if not commit_is_since(commit, date_since) ]
            commits_per_date = len(repo_commits)
            commit_history.append(commits_per_date)
        plt.plot(dates, commit_history, label=repo)
        plt.legend()
    return plt
