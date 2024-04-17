"""Handles CLI aruments."""

import argparse

parser = argparse.ArgumentParser(description="Compare histories git repositories.")

parser.add_argument('-y', '--y-unit')

parser.add_argument('-x', '--x-unit')

parser.add_argument('-m', '--max_commits')

parser.add_argument('-s', '--since')

parser.add_argument('plot_type',
                    metavar='plot',
                    type=str,
                    nargs='?',
                    default='line',
                    help='type of plot',
                    choices=['line', 'bar'])

parser.add_argument('repo_directory_path',
                    metavar='dir',
                    type=str,
                    nargs='+',
                    help='path to git repo')
