#!/usr/bin/python3
"""
A module that converts JSON string to python object.
"""
import json


def from_json_string(my_str):
    """
    A deserializer that converts json to python object.
    """
    return json.loads(my_str)
