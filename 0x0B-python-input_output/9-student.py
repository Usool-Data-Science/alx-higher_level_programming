#!/usr/bin/python3
"""
A module that converts python object to JSON
"""


class Student:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        Converts object to json
        """
        return self.__dict__ 
