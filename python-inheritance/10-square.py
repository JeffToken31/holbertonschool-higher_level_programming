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

    def area(self):
        """
        Return area of rectangle
        """
        return self.__width * self.__height

    def __str__(self):
        """
        Format a description of object
        """
        new_str = "[Rectangle] " + str(self.__width) + "/" + str(self.__height)
        return new_str


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
