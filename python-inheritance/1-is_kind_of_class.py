"""
Function that returns True if the object is an instance of, or if the object is an instance of a class that inherited from, the specified class ; otherwise False
"""

def is_kind_of_class(obj, a_class):
    """
    Function to determine if an object is an instance or inherited from a class

    Args:
        obj: Object to check
        a_class: Class to compare
    Return:
        True: if object is an instance
        False otherwise
    """
    return True if isinstance(obj, a_class) else False
