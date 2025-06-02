#!/usr/bin/python3
"""
This module allow to append text in file
"""


def append_write(filename="", text=""):
    """
    This function is use to append text in file
    """
    with open(filename, "a", encoding="utf-8") as f:
        f.write(text)
    return len(text)
