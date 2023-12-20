#!/usr/bin/python3
"""A blue print for creating squares.
    It prints using two methods
"""


class Square(object):
    """A square blueprint that prints using both
        __str__ and my_print() function
    """
    def __init__(self, size=0, position=(0, 0)):
        """Initialize the attributes
            Attr:
                size (int): The integer value
                position (tuple): The index position
        """
        self.size = size
        self.position = position

    def __str__(self):
        """A printer for the class.
            It prints in similar way like my_print()
        """
        my_result = self.my_print()
        return my_result

    @property
    def size(self):
        """Protect the size attribute by making it
            a private attribute
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Ensures that the value of size is only a
            positive integer.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        """Protects the position argument by making it
            a private attribute
        """
        return self.__position

    @position.setter
    def position(self, value):
        """Ensure the position arguments takes only tuple
            with exactly 2 positive integer values
        """
        if (not isinstance(value, tuple) or
                not all(x >= 0 for x in value) or
                not all(isinstance(x, int) for x in value) or
                len(value) != 2):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """Returns the area of the squre.
            It is computed as size ** 2
        """
        return self.__size ** 2

    def my_print(self):
        """Prints the string obtained by concatinating all results
            together into a single string. It shares performance
            with the __str__().
        """
        result = ""
        for i in range(self.__position[1]):
            result += "\n"
        for i in range(self.__size):
            for j in range(self.__position[0]):
                result += " "
            for k in range(self.__size):
                result += "#"
            result += "\n"
        result = result[:-1]  # Remove the last new line
        return result
