#!/usr/bin/python3
"""
A module that converts class to JSON
"""


def class_to_json(obj):
    """
    Converts class to JSON
    """
    return vars(obj)
