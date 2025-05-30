#!/usr/bin/python3
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
        print("{}".format(text[i]), end="")
        if text[i] in ".?:":
            print("\n")
            i += 1
            if i < len(text) and text[i] == " ":
                while text[i] == " ":
                    i += 1
        else:
            i += 1
