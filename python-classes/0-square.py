"""Square Class.

This module contains a class that defines a square.

Usage Example:

    Square = __import__('1-square').Square

    my_square = Square(3)
    print(type(my_square))
    print(my_square.__dict__)
"""

class Square:
    """Defines the blueprint of a Square

    Attribute:
        size: Integer indicating the size of the object.
    """

    def __init__(self, size):
        """
        Object constructor method
        Initializes Square with size

        Arg:
            size: Integer indicating the size of the object
        """
        self.__size = size
