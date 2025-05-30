#!/usr/bin/python3
from sys import stderr


def safe_function(fct, *args):
    try:
        result = fct(*args)
    except (ZeroDivisionError, IndexError) as error:
        print("Exception: {}".format(error), file=stderr)
        result = None
    return result
