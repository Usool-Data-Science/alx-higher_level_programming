#!/usr/bin/python3
"""
A test class for our maximum function
It Iterate over a list and
return the maximum value from it
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMax(unittest.TestCase):
    """
    Checks for various type of function edge cases
    """
    def test_max_integer(self):
        """
        Checks for possible edge cases for max_integer function
        """
        self.assertEquals(max_integer([1, 3, 5]), 5)
        self.assertEquals(max_integer([3]), 3)
        self.assertRaises(TypeError, max_integer, 3)
        self.assertRaises(TypeError, max_integer, None)
