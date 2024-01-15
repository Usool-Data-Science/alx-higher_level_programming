#!/usr/bin/python3
"""
A module that simulate a rectangle by
inheriting from a base shape.
"""
from models.base import Base

class Rectangle(Base):
    """
    A blueprint for a rectangle.
    """
    def __init__(self, width, height, x=0, y=0, id=None):
    """
    Instantiates the rectangle object upon each call.
    """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Privatizes the width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Safeguard the width attribute"""
        self.int_validation('width', value)
        self.__width = value

    @property
    def height(self):
        """Privatizes the height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Safeguard the height attribute"""
        self.int_validation('height', value)
        self.__height = value

    @property
    def x(self):
        """Privatizes the x"""
        return self.__x

    @x.setter
    def x(self, value):
        """Safeguards the x attribute"""
        self.int_validation('x', value)
        self.__x = value

    @property
    def y(self):
        """Privatizes the y"""
        return self.__y

    @y.setter
    def y(self, value):
        """Safeguards the y attribute"""
        self.int_validation('y', value)
        self.__y = value

    def int_validation(self, name, value):
        """Compare the value input again an int standard"""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if (name == "height" or name == "width") and value <= 0:
            raise ValueError("{} must be > 0".format(name))
        if (name == "x" or name == "y") and value < 0:
            raise ValueError("{} must be >= 0".format(name))

    def area(self):
        """Defines the area of the rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """Prints the unofficial string representation"""
        return "[Rectangle] ({}) {}/{} - {d}/{}".format(
            self.id, self.__x, self.__y, self.__width,
            self.height)

    def to_dictionary(self):
        """A dictionary converter"""
        myDict = {}
        for key in 'id, width, height, x, y'.split(', '):
            myDict[key] = getattr(self, key)

         return myDict
