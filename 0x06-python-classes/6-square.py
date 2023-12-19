#!/usr/bin/python3
"""A blueprint for a square.
It defines template for creating a square
"""


class Square(object):
    """A blueprint for a square.
        It defines the template for creating a square.
    """
    def __init__(self, size=0, position=(0, 0)):
        """Initialize a square instance.
            Args:
                size (int): Size of the square
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Protects the size from unauthorize access.
            Its setter property below, ensures the size
            is of type int, otherwise it raises the appropriate
            error message.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """This documentation has already being stated in its
            getter function doc.
            Please check above.
        """
        if isinstance(value, int) is False:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        """Protects the position attribute from an unauthorize
            acces.
        """
        return self.__position

    @position.setter
    def position(self, value):
        """Ensures appropriate definition of the position
            attribute of our square.
        """
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            # If all this condition are true raise an exception
            raise TypeError(
                    "position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """Estimates the area of a Square
            Return:
                Area of the square
        """
        return self.__size ** 2

    def my_print(self):
        """This is a Square printer
            It prints a square shape with `#`
        """
        if self.__size > 0:
            [print("") for j in range (0, self.__position[1])]
            for i in range(self.__size):
                print("{}".format('_' * self.__position[0]), end="")
                print("{}".format('#' * self.__size), end="")
                print("{}".format(""))
        else:
            print("{}".format(""))
