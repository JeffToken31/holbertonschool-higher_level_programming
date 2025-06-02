#!/usr/bin/python3
"""
This module allow to write an object to a file using json representation
"""
import json


def from_json_string(my_str):
    """
    Function to write an object to a file using json representation
    """
    return json.loads(my_str)
