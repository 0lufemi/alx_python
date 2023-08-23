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
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.__width}"

    @property
    def size(self):
        return self.__width

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value <= 0:
            raise ValueError("size must be > 0")
        self.__height = value
        self.__width = value
