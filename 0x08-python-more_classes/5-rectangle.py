#!/usr/bin/python3
"""
A module for calculating area and perimeter
"""


class Rectangle(object):
    """
    A blue-print for calculating area and perimeter
    """
    def __init__(self, width=0, height=0):
        """
        Initialize an instance upon every call.
        Args:
            widht (int): The width of the rectangle
            height (int): The height of the rectangle
        Return: None
        """
        self.width = width
        self.height = height

    def __str__(self):
        """
        Return and executable string format.
        """
        result = f""
        for i in range(self.height - 1):
            result += "#" * self.width
            result += '\n'
        result += "#" * self.width

        return result

    def __repr__(self):
        """
        Official representation of the string.
        """
        return "{}({}, {})".format((type(self).__name__), self.__width, self.__height)

    def __del__(self):
        """
        To delete an instance
        """
        print("Bye rectangle...")

    @property
    def width(self):
        """
        Privatize the attribute width
        Return:
            A private width attribute
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Declare some predefined set of rules for width
        """
        if not (isinstance(value, int)):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """
        Privatize the attribute height
        Return:
            A private height attribute
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Declare some predefined set of rules for height.
        """
        if not (isinstance(value, int)):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """
        Computes the area of the rectangle
        """
        return self.height * self.width

    def perimeter(self):
        """
        Computes the perimeter of the rectangle
        """
        if self.width == 0 or self.height == 0:
            return 0
        else:
            return 2 * (self.width + self.height)
