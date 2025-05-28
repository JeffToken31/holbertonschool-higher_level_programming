#!/usr/bin/python3
"""
This module is just a class
"""


class BaseGeometry:
    """
    Parent class for futur class
    """
    def area(self):
        """
        Calcul area of object
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Check if instance is an integer non negative
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


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
