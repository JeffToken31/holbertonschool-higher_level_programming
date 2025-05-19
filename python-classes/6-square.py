#!/usr/bin/python3
"""
This module Allow to learn POO with class
"""


class Square:
    """
    Define a class named Square
    """
    def __init__(self, size=0, position=(0, 0)):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
        if (
            not isinstance(position, tuple)
            or not isinstance(position[0], int)
            or not isinstance(position[1], int)
            or len(position) != 2
            or position[0] < 0
            or position[1] < 0
        ):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = position

    def area(self):
        return self.__size * self.__size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        """
        Setter
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        """
        Setter
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
        if self.__size == 0:
            print()
        else:
            print("\n" * self.__position[1], end="")
            for i in range(self.__size):
                print(" " * self.__position[0], end="")
                print("#" * self.__size)
