import os
from pathlib import Path
from datetime import datetime, timedelta, timezone
import time

from .cli import parser
from .git_tools import find_repositories

CODE_REPOSITORY = Path(__file__).parent.parent.parent


def main(max_commits: int = 1000, since: timedelta = timedelta(days=7)):
    args = parser.parse_args()
    repos: list[Repo] = find_repositories(args.repo_directory_path)
    
    repo_dict: dict = {}
    for repo in repos:    
        commits = get_commits(repo, commits = max_commits)
        recent_commits = [commit for commit in commits if commit_is_since(commit, since)]
        print(repo, recent_commits)
        repo_dict[clean_repo_name(repo)] = recent_commits

    return repo_dict



        
