"""
Unit testing for song
"""
import unittest
from song import startNum

class testsongnumber(unittest.TestCase):
    def test_number(self):
        self.assertTrue(type(startNum) == int)
        self.assertIsNot(type(startNum),bool)
