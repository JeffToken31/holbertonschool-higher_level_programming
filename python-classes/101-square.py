#!/usr/bin/python3
"""
This module Allow to learn POO with class
"""


class Square:
    """
    Define a class named Square by its size and position
    """
    def __init__(self, size=0, position=(0, 0)):
        """
        Initialize a square by a size and position given
        args:
            size(int): to define size of square
            positon(tuple): to define a position with x and y values
        raises:
            TypeError: (
                        if size isn't an integer
                        or position haven't a valid tuple
                        )
            ValueErroe: if size is less than 0
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
        if (
            not isinstance(position, tuple)
            or len(position) != 2
            or not isinstance(position[0], int)
            or not isinstance(position[1], int)
            or position[0] < 0
            or position[1] < 0
        ):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = position

    def area(self):
        """
        Return area of square
        """
        return self.__size * self.__size

    @property
    def size(self):
        """
        Get the size of square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Set a size of square
        args:
            value(int): to define size of square
        raises:
            TypeError: if value is an integer
            ValueErroe: if value is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        """
        Get the position x and y of square
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Set a position of square
        args:
            value(tuple): to define the position x and y of square
        raises:
            TypeError: if value isn't a tuple with two positifs integer
        """
        if (
            not isinstance(value, tuple)
            or not isinstance(value[0], int)
            or not isinstance(value[1], int)
            or len(value) != 2
            or value[0] < 0
            or value[1] < 0
        ):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def my_print(self):
        """
        Print a square made of hash at psition given:
        Verticaly by adding new lines and Honrizontaly by addig new spaces
        """
        if self.__size == 0:
            print()
        else:
            print("\n" * self.__position[1], end="")
            for i in range(self.__size):
                print(" " * self.__position[0], end="")
                print("#" * self.__size)

    def __str__(self):
        """
        Return a rectangle made of hashes
        """
        new_str = "\n" * self.__position[1]
        for i in range(self.__size):
            new_str += " " * self.__position[0]
            new_str += "#" * self.__size
            if i != self.__size - 1:
                new_str += "\n"
        return new_str
