#!/usr/bin/python3
"""
    A function that multiplies
    a number to each element of a list
"""


def multiply_list_map(my_list=[], number=0):
    new_list = list(map(lambda a: a*number, my_list))
    return (new_list)
