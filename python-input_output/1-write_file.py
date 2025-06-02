#!/usr/bin/python3
"""
This module allow to write in file
"""


def write_file(filename="", text=""):
    """
    Function to write in a file
    """
    with open(filename, "w", encoding="utf-8") as f:
        f.write(text)
        return len(text)
