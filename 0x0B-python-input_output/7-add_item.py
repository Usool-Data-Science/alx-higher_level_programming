#!/usr/bin/python3
"""
A module that adds all argument from the
command line to a JSON file.
"""
import json
import sys
import os


save_to_json_file = __import__(
        '5-save_to_json_file').save_to_json_file
load_from_json_file = __import__(
        '6-load_from_json_file').load_from_json_file
filename = 'add_item.json'
result = []

if os.path.exists(filename):
    result = load_from_json_file(filename)

for index in sys.argv[1:]:
    result.append(index)

save_to_json_file(result, filename)
