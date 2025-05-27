#!/usr/bin/python3
from abc import ABC, abstractmethod
from math import pi
"""
This module use duck typing concept to create subclasses and adapted methods
"""
class Shape(ABC):
    """
    Mother class to def methods for subclasses
    """
    @abstractmethod
    def area(self):
        """
        Method who allow to calcul area of childrens classes
        """
        pass

    @abstractmethod
    def perimeter(self):
        """
        Method who allow to calcul perimeter of childrens classes
        """
        pass

class Circle(Shape):
    """
    Circular object class
    """
    def __init__(self, radius=0):
        if type(radius) is not int:
            raise TypeError("{} must be an integer".format(radius))
        if radius <= 0:
            raise ValueError("{} must be greater than 0".format(radius))
        self.__radius = radius

    def area(self):
        """
        Define area of a circle
        """
        return (self.__radius * self.__radius) * pi
    
    def perimeter(self):
        """
        Define area of a circle
        """
        return (2 * self.__radius) * pi
    
class Rectangle(Shape):
    """
    Rectancle object class
    """
    def __init__(self, width=0, height=0):
        """
        Inisilize a Rectancle
        """
        if type(width) is not int:
            raise TypeError("{} must be an integer".format(width))
        if width <= 0:
            raise ValueError("{} must be greater than 0".format(width))
        self.__width = width

        if type(height) is not int:
            raise TypeError("{} must be an integer".format(height))
        if height <= 0:
            raise ValueError("{} must be greater than 0".format(height))
        self.__height = height


    def area(self):
        """
        Define area of a rectangle
        """
        return self.__width * self.__height
    
    def perimeter(self):
        """
        Define area of a rectangle
        """
        return (self.__width * 2) + (self.__height * 2)

def shape_info(obj):
    print("Area: {}".format(obj.area()))
    print("Perimeter: {}".format(obj.perimeter()))