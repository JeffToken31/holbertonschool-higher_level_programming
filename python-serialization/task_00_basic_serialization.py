#!/usr/bin/python3
"""
This module allow two fonction: Serialize and save to file
and load and deserialize a file
"""
import json


def serialize_and_save_to_file(data, filename):
    """
    This function serialize and save to a file data
    """
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f)


def load_and_deserialize(filename):
    """
    This function load and deserialize a file
    """
    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)
