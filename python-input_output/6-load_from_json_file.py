#!/usr/bin/python3
"""
This module allow to deserialize an object from json file
"""
import json


def load_from_json_file(filename):
    """
    Function that deserialize an object from json file
    """
    with open(filename, "r", encoding="utf-8") as f:
        return json.loads(f.read())
