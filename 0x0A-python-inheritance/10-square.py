#!/usr/bin/python3
Rectangle = __import__('9-rectangle').Rectangle
"""
Check for inheritance
"""


class Square(Rectangle):
    """
    A blueprint for a Square
    """

    def __init__(self, size):
        """
        Initializes the rectangle
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(self.__size, self.__size)

    def __repr__(self):
        return "[Rectangle] {}/{}".format(self.__size, self.__size)
