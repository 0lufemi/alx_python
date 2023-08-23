"""
Module Rectangle
Create a Rectangle class inheriting from Base
"""

from models.base import Base

class Rectangle(Base):
    """
    class describing a rectangle
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initializes the rectangle instance
        Args:
            __width:
            __height:
            __x:
            __y:
        """

        super().__init__(id)

        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def __str__(self):
        """Returns a formatted string"""
        return f"[Rectangle] ({self.id}) {self.__x}/{self.__y} - {self.__width}/{self.__height}"

    @property
    def width(self):
        """Retrieves the width"""

        return self.__width

    @width.setter
    def width(self, value):
        """Sets the width"""

        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value


    @property
    def height(self):
        """Retrieves the height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets the height"""

        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Retrieves the x attribute"""
        return self.__x

    @x.setter
    def x(self, value):
        """Sets the x attribute"""

        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Retrieves the y attribute"""
        return self.__y

    @y.setter
    def y(self, value):
        """Sets the y attribute"""

        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Returns the area of the rectangle"""

        return self.__width * self.__height

    def display(self):
        """
        Method that prints out the Rectangle instance with '#'
        """
        for y in range(self.__y):
            print()
        for i in range(self.__height):
            print(" " * self.__x, end="")
            for j in range(self.__width):
                print("#", end="\n" if j == self.__width - 1 else "")

    def update(self, *args, **kwargs):
        """Updates attribute of an instance"""

        if len(args) >= 1:
            self.id = args[0]
        elif "id" in kwargs:
            self.id = kwargs["id"]

        if len(args) >= 2:
            self.width = args[1]
        elif "width" in kwargs:
            self.width = kwargs["width"]

        if len(args) >= 3:
            self.height = args[2]
        elif "height" in kwargs:
            self.height = kwargs["height"]

        if len(args) >= 4:
            self.x = args[3]
        elif "x" in kwargs:
            self.x = kwargs["x"]

        if len(args) >= 5:
            self.y = args[4]
        elif "y" in kwargs:
            self.y = kwargs["y"]
