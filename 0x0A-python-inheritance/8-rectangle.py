#!/usr/bin/python3
BaseGeometry = __import__('7-base_geometry').BaseGeometry
"""
Check for inheritance
"""


class Rectangle(BaseGeometry):
    """
    A blueprint for a rectangle
    """

    def __init__(self, width, height):
        """
        Initialize the rectangle
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

