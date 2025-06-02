#!/usr/bin/python3
"""
This module allow to serialize a object in json
"""
import json


def to_json_string(my_obj):
    """
    This function serialize an object in json file
    """
    return json.dumps(my_obj)
