#!usr/bin/python3
"""
This module allows testing a function that prints a indeted text
"""

def text_indentation(text):
    """
    This function prints a indeted text
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    i = 0
    while i < len(text):
        if text[i] in ".?:":
            print("{}\n".format(text[i]))
            i += 2
        else:
            print("{}".format(text[i]), end="")
            i += 1