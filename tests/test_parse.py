import unittest
from app.parse import parse_design_doc

class TestParse(unittest.TestCase):
    def test_parse_base_design(self):
        parse_design_doc("test")
