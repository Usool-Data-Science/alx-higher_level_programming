#!/usr/bin/python3
"""
A function that print the name of a user
It takes 2 arguments:
firstName and the Second Name
"""


def say_my_name(first_name, last_name=""):
    """
    A function that prints the name of a user
    """
    if not (isinstance(first_name, str)):
        raise TypeError("first_name must be a string")
    if not (isinstance(last_name, str)):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
