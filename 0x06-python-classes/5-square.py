#!/usr/bin/python3
"""2. Size validation"""


class Square:
    """This is a square"""

    def __init__(self, size=0):
        """initializing the square"""
        self.__size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, size):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        return self.__size * self.__size

    def my_print(self):
        if self.__size == 0:
            print()

        for i in range(self.__size):
            print("#" * self.__size)
