from git import Repo, Commit, GitError
import os
from datetime import datetime, timedelta
import time

CODE_REPOSITORY = os.path.abspath("/home/natalie/code/")

def find_repositories(dirpath: str = CODE_REPOSITORY) -> list[Repo]:
    repos: list[Repo] = []
    for child in os.listdir(dirpath):
        child_path = os.path.join(dirpath, child)
        if os.path.isdir(child_path):
            try:
                print("isdir" + child)
                repo = Repo(child_path)
            except GitError:
                print(child_path + " was no correctly loaded!")
                print(GitError)
            else:
                repos.append(repo)
        else:
            print("noisdir" + child)

    return repos

def get_commits(repo: Repo, commits: int = 1, since: int = 7) -> list[Commit]:
    print("weee")
    repo_commits = repo.iter_commits("master", max_count=commits)
    print(repo_commits)

    return list(repo_commits)

def main():
    repos: list[Repo] = find_repositories()

if __name__ == "__main__":
    main()


        
