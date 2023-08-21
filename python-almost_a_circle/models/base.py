"""
Module Base
Base class for all other classes in this project
"""

class Base:
    """
    Base class
    Private class attribute: __nb_objects
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initializes the instance
        Args:
            id: id of the instance
        """

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
