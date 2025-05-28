#!/usr/bin/python3
"""
This module is just a class
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    inheritance class of BaseGeometry
    """
    def __init__(self, size):
        """
        Initialize a square by a size given
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """
        Return area of square
        """
        return self.__size * self.__size
