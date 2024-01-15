#!/usr/bin/python3
"""
A module with a blue print from upcoming fucntions.
"""


class Base(object):
    """
    A blue print for upcoming function.
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Instantiates the class upon every call.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects


