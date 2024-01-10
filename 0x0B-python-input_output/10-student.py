#!/usr/bin/python3
"""
A module that prints the dictionary representation of students'
class
"""


class Student(object):
    """
    A Blue-print for student qualities.
    """

    def __init__(self, first_name, last_name, age):
        """
        An instantiator for the object
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Prints the dictionary representation of Student object
        """
        if attrs is None:
            return self.__dict__
        my_dict = {}
        for k,v in self.__dict__.items():
            if k in attrs:
                my_dict[k] = v
        return my_dict
