#!/usr/bin/python3
"""
A module for defining the blue-print of a rectangle object
"""


class Rectangle(object):
    """
    A rectangle blue-print for defining other
    rectangles.
    """
    def __init__(self, width=0, height=0):
        """
        An instantiator for each object instance.
        Args:
            width (int): The width of the object.
            height (int): The height of the object.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        Declares the width as a private attribute.
        Return:
            A private value for width.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Set predefined condition(s) for the width attribute.
        """
        if not (isinstance(value, int)):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be greater >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """
        Declares the height as a private attributes.
        Return:
            A private attribute for height.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Set predefined condition(s) for the height attribute.
        """
        if not (isinstance(value, int)):
            raise TypeError("height must be an integer")
        elif (value < 0):
            raise ValueError("height must be >= 0")
        else:
            self.__height = value
