#!/usr/bin/python3
"""This module creates a blueprint(class) for a circle
The blueprint assigns size to the circle instances
"""


class Square(object):
    """A blueprint for squares
       It has only one argument and it is size.
    """
    def __init__(self, size=0):
        """Instantiate a circle with size
           Args:
               size (int): The size of the circle.
        """
        if isinstance(size, int) is False:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
