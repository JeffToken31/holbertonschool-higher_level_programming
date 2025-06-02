#!/usr/bin/python3
"""
This module allow to write an object to a file using json representation
"""
import json


def save_to_json_file(my_obj, filename):
    """
    Function to write an object to a file using json representation
    """
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(my_obj, f)
