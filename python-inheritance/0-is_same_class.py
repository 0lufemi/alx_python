def is_same_class(obj, a_class):
    """
    Function to determine if obj is an instance of a_class

    Args:
        obj
        a_class
    Returns:
        True if obj is an instance of a_class
        False otherwise
    """
    return True if type(obj) == a_class else False
