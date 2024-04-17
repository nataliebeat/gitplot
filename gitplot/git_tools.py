""" Functions using git-python to retrieve data from the listed repositories."""

from datetime import datetime, timedelta, timezone
from git import Repo, Commit, GitError

def clean_repo_name(repo: Repo) -> str:
    """Return the last directory in the filepath."""
    path = repo.working_tree_dir
    return str(path).rsplit('/', maxsplit=1)[-1]

def find_repositories(repo_list: list[str]) -> list[Repo]:
    """Given a list of directories, return a list of Git-Python Repositories"""
    repos: list[Repo] = []
    for repo_directory in repo_list:
        try:
            repo = Repo(repo_directory)
        except GitError:
            print(repo_directory + " was not correctly loaded!")
        else:
            repos.append(repo)
    return repos

def get_commits(repo: Repo, commits: int = 1) -> list[Commit]:
    """Given a Git-Python repo, return a list of its commits."""
    repo_commits = repo.iter_commits(repo.active_branch, max_count=commits)
    result = list(repo_commits)
    return result

def commit_is_since(commit: Commit, since: timedelta) -> bool:
    """Return True if the commit is since a certain period of time."""
    commit_datetime = commit.committed_datetime
    my_since: timedelta = datetime.now(timezone.utc) - commit_datetime
    print(my_since)
    print(since)
    if my_since > since:
        print('f')
        return False
    print('t')
    return True

def scan_repos(repo_dirs: list[str], max_commits: int = 1000, since: timedelta = timedelta(days=7)):
    """
    Given a list of directories, return a dictionary,
    with all the information needed for plotting.
    """
    repos: list[Repo] = find_repositories(repo_dirs)
    repo_dict: dict = {}
    for repo in repos:
        commits = get_commits(repo, commits = max_commits)
        recent_commits = [commit for commit in commits if commit_is_since(commit, since)]
        print(repo, recent_commits)
        repo_dict[clean_repo_name(repo)] = recent_commits

    return repo_dict
