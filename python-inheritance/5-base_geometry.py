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
        self.name = name
        self.value = value

        isinstance(self.name, str)

        if not isinstance(self.value, int):
            raise TypeError(f"{self.name} must be an integer")
        if self.value <= 0:
            raise ValueError(f"{self.name} must be greater than 0")
