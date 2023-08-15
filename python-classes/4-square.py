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
        """
        Gets the size private attribute value.

        Returns:
            The size private attribute
        """
        
        return self.__size

    @size.setter
    def size(self, value):
        """
        Sets the size private attribute value.

        Validates the assignment of the size private attribute.

        Arg:
            value: the value to be set
        """

        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        A public object method

        Returns:
            square area
        """

        return self.__size ** 2

    def my_print(self):
        """
        Displays the square object filled with #
        """

        if self.__size == 0:
            print()
        else:
            for _ in range(self.__size):
                print("#" * self.__size)
