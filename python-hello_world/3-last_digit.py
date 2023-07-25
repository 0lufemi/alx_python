# import random
# number = random.randint(-10000, 10000)

# last_digit = abs(number) % 10

# if number < 0:
#     print(f"Last digit of {number} is -{last_digit} and is less than 6 and not 0")
# elif number == 0:
#     print(f"Last digit of {number} is {last_digit} and is 0")
# else:
#     if last_digit > 5:
#         print(f"Last digit of {number} is {last_digit} and is greater than 5")
#     elif last_digit == 0:
#         print(f"Last digit of {number} is {last_digit} and is 0")
#     else:
#         print(f"Last digit of {number} is {last_digit} and is less than 6 and not 0")

import random
number = random.randint(-10000, 10000)

def get_last_digit_info(number):
    last_digit = number % 10

    if number < 0:
        return "and is less than 6 and not 0"
    else:
        if last_digit > 5:
            return "and is greater than 5"
        elif last_digit == 0:
            return "and is 0"
        else:
            return "and is less than 6 and not 0"

def main():
    output_string = f"Last digit of {number} is {abs(number) % 10} {get_last_digit_info(number)}"
    print(output_string)

if __name__ == "__main__":
    main()
