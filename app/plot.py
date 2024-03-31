import matplotlib.pyplot as plt

from .main import main

git_data = main()

repos = git_data.keys()
commits = git_data.values()

plt.figure(figsize=(9,4))
plt.bar(git_data.keys(), git_data.values())
plt.show()
