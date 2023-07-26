def validate_password(password):
    if len(password) < 8:
        return False

    if ' ' in password:
        return False

    upper = False
    lower = False
    digit = False

    for char in password:
        if char.isupper():
            upper = True
        elif char.islower():
            lower = True
        elif char.isdigit():
            digit = True

    return upper and lower and digit
