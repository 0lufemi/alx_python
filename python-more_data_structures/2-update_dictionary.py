def update_dictionary(a_dictionary, key, value):
    # Checks if key is not present in the dictionary
    if key not in a_dictionary:
        a_dictionary[key] = value
    # checks if key is already in dictionary
    else:
        for i in a_dictionary:
            if i == key:
                a_dictionary[i] = value

    return a_dictionary
