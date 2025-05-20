#!/usr/bin/python3
"""
This module Allow to learn POO with class
"""


class Rectangle:
    """
    Define a class named Rectangle
    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """
        Initialize a rectangle by a width and height given
        args:
            width(int): to define width of the rectangle
            height(int): to define height of the rectangle
        raises:
            TypeError: if width and height aren't an integer
            ValueErro: if size is less than 0
        """
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        elif width < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = width

        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        elif height < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """
        Get the width of the rectangle
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Set a width of the rectangle
        args:
            value(int): to define width of the rectangle
        raises:
            TypeError: if value is an integer
            ValueErroe: if value is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """
        Get the height of the rectangle
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
    Set a height of the rectangle
        args:
            value(int): to define height of the rectangle
        raises:
            TypeError: if value is an integer
            ValueErroe: if value is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """
        Return area of rectangle
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        Return the perimeter of the rectangle
        """
        if self.width == 0 or self.height == 0:
            return 0
        return (self.__width * 2) + (self.height * 2)

    def __str__(self):
        """
        Return a rectangle made of hashes
        """
        new_str = ""
        symbol = str(self.print_symbol)
        if self.__width == 0 or self.__height == 0:
            return new_str
        else:
            i = 0
            while i < self.height:
                new_str += symbol * self.width
                if i != self.height - 1:
                    new_str += "\n"
                i += 1
            return new_str

    def __repr__(self):
        """
        Return a rectangle made of hashes
        """
        if self.__width == 0 or self.__height == 0:
            return ""
        else:
            return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """
        Delete last rectangle and print a message
        """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        area_1 = rect_1.area()
        area_2 = rect_2.area()
        if area_1 >= area_2:
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        return cls(size, size)
