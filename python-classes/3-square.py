"""
Class Square
This module contains a class that defines a square
"""

class Square:
    """
    Defines the blueprint of a square
    """

    def __init__(self, size=0):
        """
        Initializes square with size
        Args:
            size: integer indicating the size of square
        Raises:
            TypeError: if size is not an integer
            ValueError: if size is less than 0
        """

        self.size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        return self.__size ** 2
