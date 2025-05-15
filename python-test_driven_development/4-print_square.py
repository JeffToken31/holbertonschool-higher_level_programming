#!/usr/bin/python3
"""
This module allows testing a function that print a square made of hashes
"""


def print_square(size):
    """
    This function prints a square made of hash with a specified size
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    for i in range(size):
        print("#" * size)
