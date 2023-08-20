"""
class BaseGeometry
"""

class BaseGeometry:
    """
    class definition: BaseGeometry

    Method:
        area
        integer_validator
            Args:
                name:
                value:
    """
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        isinstance(name, str)

        if not isinstance(value, int):
            raise TypeError("<name> must be an integer")
        if value <= 0:
            raise ValueError("<name> must be greater than 0")
