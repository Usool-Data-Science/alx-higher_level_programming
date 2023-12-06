#!/usr/bin/python3
"""
    A function for replacing a value in a list
"""


def search_replace(my_list, search, replace):
    new_list = [replace if search == x else x for x in my_list]
    return (new_list)
