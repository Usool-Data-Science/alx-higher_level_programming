#!/usr/bin/python3
"""
A module for converting python object to JSON
"""
import json


def to_json_string(my_obj):
    """
    An object converter to JSON
    """
    return json.dumps(my_obj)
