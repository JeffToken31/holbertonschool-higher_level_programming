#!/usr/bin/python3
"""
This module is just a class
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry

class Rectangle(BaseGeometry):
    """
    inheritance class of BaseGeometry
    """
    def __init__(self, width, height):
        """
        Initialize a rectangle by a width and height given
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
