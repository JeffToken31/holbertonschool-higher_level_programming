#!/usr/bin/python3
"""
Module who's test a function who print a name
"""


def say_my_name(first_name, last_name=""):
    """
    Print a complete Name (first name, last name) in this order
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
