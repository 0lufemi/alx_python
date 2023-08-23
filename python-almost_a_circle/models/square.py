"""
Square class that inherits from the Rectangle class
"""

from models.rectangle import Rectangle

class Square(Rectangle):
    """
    class Square
    Inherits from:
        Rectangle
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        Instantiates the Square class
        Args:
            size
            x
            y
            id
        """

        super().__init__(size, size, x, y, id)
        self.size = size

    def __str__(self):
        """Returns a formatted string"""

        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.__width}"

    @property
    def size(self):
        """Gets the square size"""

        return self.__width

    @size.setter
    def size(self, value):
        """Sets the square size"""

        self.__height = value
        self.__width = value
