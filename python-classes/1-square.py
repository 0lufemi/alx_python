"""
Class Square
This module contains a class that defines a square
"""

class Square:
    """
    Defines the blueprint of a square

    Attribute:
        size: Integer indicating size of square
    """

    def __init__(self, size=0):
        """
        Initializes square with size

        Arg:
            size: Integer indicating size of square
                  Has a default value of 0
            Raises:
                TypeError: If size is not an integer
                ValueError: If size < 0
        """
        self.__size = size
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
