import unittest
from unittest.mock import patch

from gitsome.cli import parser

class TestCliArgs(unittest.TestCase):
    def test_repo_directory_path(self):
        args = parser.parse_args(args=['../cribbage'])
        print(args)

