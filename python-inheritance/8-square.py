"""Program that defines a class Square that inherits from Rectangle"""

Rectangle = __import__('7-rectangle').Rectangle

class Square(Rectangle):
    """Class Square that inherits from Rectangle"""

    def __init__(self, size):
        """Initializes an instance
        Args:
            size: size of the square"""

        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        """Returns a formatted string"""

        return f"[Rectangle] {self.__size}/{self.__size}"
