#!/usr/bin/python3
"""
A module that dump a python object into a JSON file.
"""
import json


def save_to_json_file(my_obj, filename):
    """
    A serializer into a file called filename.
    """
    with open(filename, mode='w', encoding='utf-8') as file:
        json.dump(my_obj, file)
