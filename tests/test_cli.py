import unittest
from unittest.mock import patch

from argparse import ArgumentError

from gitplot.cli import parser


class TestCliArgs(unittest.TestCase):
    def test_repo_directory_path(self):
        args = parser.parse_args(args=['../cribbage'])
        self.assertEqual(args.repo_directory_path, ['../cribbage'])
    
    def test_plot_type(self):
        args = parser.parse_args(args=['line', '../cribbage', '.'])
        self.assertEqual(args.plot_type, 'line')
        self.assertEqual(args.repo_directory_path, ['../cribbage', '.'])

    def test_incorrect_plot_type(self):
        def parse_badone():
            return parser.parse_args(args=['hehe', '../cribbage'])
        self.assertRaises(ArgumentError,  parse_badone)

