import matplotlib.pyplot as plt

from .main import main

git_data = main()

def plot_repo_by_commit_count():
    repos = list(git_data.keys())
    repo_commits = git_data.values()
    commit_count = [len(commits) for commits in repo_commits]
    plt.figure(figsize=(9,4))
    plt.bar(repos, commit_count)
    return plt
