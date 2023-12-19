#!/usr/bin/python3
"""A class that assign a size to a circle.
"""


class Square(object):
    """A class that assign size to a circle.
       Args:
           size (int): The size of the circle.
       Attributes:
           size (int): The size of the circle.
    """
    def __init__(self, size):
        """ The circle initiator with a specific size.
        """
        self.__size = size  #: The size of the circle
