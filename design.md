# Gitsome

Analyzes git repos' commit history to compare progress between projects.

## Program Flow

### Initialize
Scan repositories listed in settings.
- main.scan_repos()
    - settings.repo_dirs
    - git_api.scan_repos()-> Repo

### Process Commandline Arguments

See arguments dict 
- main.process_arguments()

### Arguments:

- plot | plot.plot()
    - (s) since_days: int = 100 | git_api.commits_since_days() -> list(Commit)
    - (y) measure_y: enum{commits, lines_changed} = commits | git_api.process_commits \
    -> dict(datetime.strf(committed_date):measure_y)
        - commits | cumulate_commits() -> int: commits += 1
        - lines_changed | cumulate_lines_changed() 
            - git_api.process_commit_data() -> int: lines_changed += lines_of(data)



