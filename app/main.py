from git import Repo
import os

CODE_REPOSITORY = os.path.abspath("/home/natalie/code/")

def find_repositories(dirpath: str = CODE_REPOSITORY) -> list[Repo]:
    repos: list[Repo] = []
    for child in os.listdir(dirpath):
        if os.path.isdir(child):
            repo = Repo(child)
            #except :
            repos.append(repo)

    return repos

        
