"""Program with class Rectangle that inherits from BaseGeometry"""

BaseGeometry = __import__('5-base_geometry').BaseGeometry

class Rectangle(BaseGeometry):
    """Defines a rectangle class
    Private instance attributes:
        width
        height"""

    def __init__(self, width, height):
        """Initializes an instance
        Args:
            width: width of the Rectangle
            height: height of the Rectangle"""

        self.__width = width
        self.__height = height
        self.integer_validator("width", width)
        self.integer_validator("height", height)

    def __str__(self):
        """returns a formatted string"""

        return f"[Rectangle] {self.__width}/{self.__height}"

    def area(self):
        """Computes the area of the rectangle"""

        return self.__height * self.__width
