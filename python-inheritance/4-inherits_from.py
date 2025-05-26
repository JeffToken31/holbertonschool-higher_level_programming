#!/usr/bin/python3
"""
This module is used to check if an instance of a class inherit is same
"""
def inherits_from(obj, a_class):
    """
    Function to check if an instance of a class inherit is same
    """
    if type(obj) is a_class:
        return False
    return True
