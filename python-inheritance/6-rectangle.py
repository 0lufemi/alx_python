"""
Program with class Rectangle that inherits from BaseGeometry (5-base_geometry.py).
"""

BaseGeometry = __import__('5-base_geometry').BaseGeometry

class Rectangle(BaseGeometry):
    """
    defines a Rectangle class
    Private instance attributes:
        width
        height
    """
    def __init__(self, width, height):
        """Initializes an instance
        Args:
            width: width of the Rectangle
            height: height of the Rectangle"""

        self.__width = width
        self.__height = height
        self.integer_validator("width", width)
        self.integer_validator("height", height)
