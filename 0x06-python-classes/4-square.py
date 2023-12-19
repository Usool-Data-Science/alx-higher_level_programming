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
        self.size = size

    def area(self):
        """ Calculates the area of the square
            Area = side ** 2
            Args:
               Takes no arguments.
            Return:
               The Area of the square
        """
        return self.__size ** 2

    @property
    def size(self):
        """This function privatizes the size of our square.
            It convert it from public attribute to private.

            Return:
                A protected size attribute.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """This is a definition guide for our size attribute.
            It ensures that the size is a valid integer otherwise
            it raise the appropriate error.
        """
        if isinstance(value, int) is False:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value
