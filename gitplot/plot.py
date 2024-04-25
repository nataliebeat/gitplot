"""Plots data from git directories using the .git_tools module and matplotlib"""
import logging 

from datetime import datetime, timedelta, timezone
import matplotlib.pyplot as plt
from .git_tools import scan_repos, commit_is_since

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG)

def plot_repo_by_commit_count(repo_dirs):
    """Plots amount of commits of given git directories"""
    git_data = scan_repos(repo_dirs)
    repos = list(git_data.keys())
    repo_commits = git_data.values()
    commit_count = [len(commits) for commits in repo_commits]
    plt.figure(figsize=(9,4))
    plt.bar(repos, commit_count)
    return plt

def plot_repo_commit_history(repo_dirs, days: int = 0):
    """Plots commit histories of given git directories since 'days' argument"""
    today = datetime.now(timezone.utc)
    if days != 0:
        git_data = scan_repos(repo_dirs, since=timedelta(days=days))
    else:
        git_data = scan_repos(repo_dirs)
        earliest_commits = []
        for repo in git_data.items():
            # gets the data of the tuple, then adds last to list of earliest commits
            logger.debug("Getting earlist commit from: %s", repo)
            earliest_commits.append(repo[1][-1].committed_datetime)
        earliest_commits = [(today - com_date).days for com_date in earliest_commits]
        days = max(earliest_commits)
    repos = list(git_data.keys())
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
