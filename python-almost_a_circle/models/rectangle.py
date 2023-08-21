"""
Module Rectangle
Create a Rectangle class inheriting from Base
"""

from base import Base

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

        self.__width = width
        self.__height =height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """Retrieves the width"""

        return self.__width

    @width.setter
    def width(self, value):
        """Sets the width"""
        self.__width = value

    @property
    def height(self):
        """Retrieves the height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets the height"""
        self.__height = value

    @property
    def x(self):
        """Retrieves the x attribute"""
        return self.__x

    @x.setter
    def x(self, value):
        """Sets the x attribute"""
        self.__x = value

    @property
    def y(self):
        """Retrieves the y attribute"""
        return self.__y

    @y.setter
    def y(self, value):
        """Sets the y attribute"""
        self.__y = value
