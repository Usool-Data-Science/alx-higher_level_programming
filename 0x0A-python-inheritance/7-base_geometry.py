#!/usr/bin/python3
"""
Check for inheritance
"""


class BaseGeometry(object):
    """
    A blueprint for base geometry
    """
    def area(self):
        """
        Just raise NotImplementedError()
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        A validator for the value
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        else:
            if value <= 0:
                raise ValueError("{} must be greater than 0".format(name))
