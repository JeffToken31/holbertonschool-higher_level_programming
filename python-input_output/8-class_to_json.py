#!/usr/bin/python3
"""
This module is use to return a dict for a json serailisation
"""


def class_to_json(obj):
    """
    Function that return a dict for a json serailisation
    """
    return obj.__dict__
