import os
from pathlib import Path
from datetime import datetime, timedelta, timezone
import time

from .cli import parser
from .git_tools import scan_repos




        



def main(max_commits: int = 1000, since: timedelta = timedelta(days=7)):
    args = parser.parse_args()
    repos = scan_repos(args.repo_directory_path)
    return repos



        
