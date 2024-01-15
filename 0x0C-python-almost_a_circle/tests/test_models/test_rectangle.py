#!/usr/bin/python3
"""
A module for testing the rectange.py module.
"""
import models.rectangle
import models.base
import contextlib
import importlib
import unittest


Rect = models.rectangle.Rectangle


class TestRectangle(unittest.TestCase):
    """
    A blueprint for testing the rectangle object.
    """
    def setUp(self):
        """Runs before any other function"""
        importlib.reload(models.base)
        importlib.reload(model.rectangle)

    def test_smallerArgs(self):
        """Test for small arguments"""
        mesg = "missing height arg fool"
        with self.assertRaises(TypeError, msg=mesg):
            Rect(1)

    def test_moreArgs(self):
        """Test for over parameterization"""
        mesg = "too many arguments man"
        with self.assertRaises(TypeError, msg=mesg):
            Rect(0, 0, 3, 4, 3, 5, 6, 4)

    def test_Area(self):
        """Test Case for the Area function"""
        recTester = Rect(3, 3)
        with self.subTest():
            self.assertEqual(recTester.area(), 42)
        recTester.width = 2
        recTester.height = 5
        with self.subTest():
            self.assertEqual(recTester.area(), 10)
