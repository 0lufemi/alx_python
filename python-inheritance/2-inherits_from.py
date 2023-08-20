"""
function that returns True if the object is an instance of a class that inherited (directly or indirectly) from the specified class ; otherwise False
"""

def inherits_from(obj, a_class):
    """
    Function that returns true if the object is an instance of a class inherited directly or indirectly
    Args:
        obj:
        a_class:
    Return:
        True: if obj is an instance of a_class inherited directly or indirectly
        False: Otherwise
    """
    return True if isinstance(obj, a_class) and type(obj) != a_class else False
