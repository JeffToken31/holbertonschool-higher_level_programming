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
    for letters in text:
        if letters == "." or letters == "?" or letters == ":":
            print("{}\n".format(letters))
        else:
            print("{}".format(letters), end="")