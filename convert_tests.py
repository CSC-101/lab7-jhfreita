import unittest
import convert
class TestCases(unittest.TestCase):

    def test_str_to_float1(self):
        self.assertEqual((convert.str_to_float('44')), 44)
    def test_str_to_float2(self):
        self.assertEqual((convert.str_to_float('twenty')), None)