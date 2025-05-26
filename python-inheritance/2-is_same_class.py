#!/usr/bin/python3
"""
This module allow to check if the object is an instance og specified class
"""


def is_same_class(obj, a_class):
    """
    Function to check if obj is instance of a specified class
    """
    if type(obj) is a_class:
        return True
    return False
