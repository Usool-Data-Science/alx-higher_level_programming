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
        Initializes the rectangle
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def __repr__(self):
        """
        Prints the official representation of the class.
        """
        return f"[{type(self).__name__}] {self.__width}/{self.__height}"

    def area(self):
        """
        Finds the area of the Rectangle
        """
        return self.__width * self.__height
