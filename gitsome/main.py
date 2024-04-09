from git import Repo, Commit, GitError
import os
from pathlib import Path
from datetime import datetime, timedelta, timezone
import time

from .cli import parser

CODE_REPOSITORY = Path(__file__).parent.parent.parent

def clean_repo_name(repo: Repo) -> str:
    path = repo.working_tree_dir
    return str(path).split("/")[-1]

def find_repositories(dirpath: Path = CODE_REPOSITORY) -> list[Repo]:
    repos: list[Repo] = []
    for child in os.listdir(dirpath):
        child_path = os.path.join(dirpath, child)
        if os.path.isdir(child_path):
            try:
                repo = Repo(child_path)
            except GitError:
                print(child_path + " was not correctly loaded!")
            else:
                repos.append(repo)

    return repos

def get_commits(repo: Repo, commits: int = 1) -> list[Commit]:
    repo_commits = repo.iter_commits("master", max_count=commits)
    result = list(repo_commits)
    return result
        



def commit_is_since(commit: Commit, since: timedelta) -> bool:
    commit_datetime = commit.committed_datetime
    my_since: timedelta = datetime.now(timezone.utc) - commit_datetime
    print(my_since)
    print(since)
    if my_since > since:
        print('f')
        return False
    else:
        print('t')
        return True

<<<<<<< HEAD
def scan_repos(max_commits: int = 1000, since: timedelta = timedelta(days=7)):
=======
def main(max_commits: int = 1000, since: timedelta = timedelta(days=7)):
    args = parser.parse_args()
    print(args.echo)
>>>>>>> 258ace3 (connect it into main() . perhaps move default list to conf files)
    repos: list[Repo] = find_repositories()
    repo_dict: dict = {}
    for repo in repos:
        commits = get_commits(repo, commits = max_commits)
        recent_commits = [commit for commit in commits if commit_is_since(commit, since)]
        print(repo, recent_commits)
        repo_dict[clean_repo_name(repo)] = recent_commits

    return repo_dict
        



        
