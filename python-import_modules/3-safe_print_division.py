def safe_print_division(a, b):
    try:
        result = a / b
    except:
        return None
    finally:
        return result
