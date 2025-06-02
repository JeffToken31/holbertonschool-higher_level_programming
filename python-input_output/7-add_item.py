#!/usr/bin/python3
"""
This module allow to keep args and store in json file
"""
import os
from sys import argv
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file

if __name__ == "__main__":
    f = "add_item.json"
    if os.path.exists(f):
        data = load_from_json_file(f)
    else:
        data = []
    args = argv[1:]
    data.extend(args)
    save_to_json_file(data, f)
