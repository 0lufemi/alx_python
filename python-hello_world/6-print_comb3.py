for number_1 in range(10):
    for number_2 in range(number_1, 10):
        if (number_1 != number_2) and (number_1 < number_2):
            print("{:1d}{:1d}".format(number_1, number_2), end="\n" if number_1 == 8 and number_2 == 9 else ", ")
