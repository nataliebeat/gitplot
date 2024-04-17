import os
from pathlib import Path
from datetime import datetime, timedelta, timezone
import time

from .cli import parser
from .plot import plot_repo_by_commit_count, plot_repo_commit_history



        



def main(max_commits: int = 1000, since: timedelta = timedelta(days=7)):
    args = parser.parse_args()
    if args.plot_type == "line":
        plot_repo_commit_history(args.repo_directory_path).show()
    else:
        plot_repo_by_commit_count(args.repo_directory_path).show()



        
