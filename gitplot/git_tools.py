""" Functions using git-python to retrieve data from the listed repositories."""
import logging

from datetime import datetime, timedelta, timezone
from git import Repo, Commit, GitError

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG)

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

def get_commits(repo: Repo, commits: int = 0) -> list[Commit]:
    """Given a Git-Python repo, return a list of its commits."""
    if commits == 0:
        logger.debug("Getting commits from %s", repo)
        repo_commits = repo.iter_commits(repo.active_branch)
    else:
        repo_commits = repo.iter_commits(repo.active_branch, max_count=commits)
    result = list(repo_commits)
    logger.debug("Commits from %s: %s", repo, len(result))
    return result

def commit_is_since(commit: Commit, since: timedelta) -> bool:
    """Return True if the commit is since a certain period of time."""
    commit_datetime = commit.committed_datetime
    my_since: timedelta = datetime.now(timezone.utc) - commit_datetime
    if my_since > since:
        return False
    return True

def scan_repos(repo_dirs: list[str], max_commits: int = 0, since: timedelta = timedelta(days=0)):
    """
    Given a list of directories, return a dictionary,
    with all the information needed for plotting.
    """
    repos: list[Repo] = find_repositories(repo_dirs)
    repo_dict: dict = {}
    for repo in repos:
        commits = get_commits(repo, commits = max_commits)
        if since.days != 0:
            commits = [commit for commit in commits if commit_is_since(commit, since)]
        repo_dict[clean_repo_name(repo)] = commits

    return repo_dict
