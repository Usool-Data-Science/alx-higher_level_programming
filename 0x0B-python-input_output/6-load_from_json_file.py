#!/usr/bin/python3
"""
A module for loading an object from a JSON file.
"""
import json


def load_from_json_file(filename):
    """
    Extract python object from a JSON file.
    """
    with open(filename, mode="r", encoding="utf-8") as file:
        return json.load(file)
