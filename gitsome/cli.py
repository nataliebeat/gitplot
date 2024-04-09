import argparse

parser = argparse.ArgumentParser(description="Compare histories git repositories.")
parser.add_argument('-y', '--y-axis')
parser.add_argument('repo_directory_path', metavar='dir', type=str, nargs='+', help='path to git repo')
