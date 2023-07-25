# Python - Hello, World

0. Hello, print
Write a Python script that prints exactly "Programming is like building a multilingual puzzle, followed by a new line.
    * Use the function print
```
guillaume@ubuntu:~/py/$ python3 0-print.py
"Programming is like building a multilingual puzzle
guillaume@ubuntu:~/py/$
```

1. Copy - Cut - Paste
Complete this 1-edges.py
    * You can find the source code 1-edges.py
    * You are not allowed to use any loops or conditional statements
    * Your program should be exactly 8 lines long
    * ```word_first_3``` should contain the first 3 letters of the variable word
    * ```word_last_2``` should contain the last 2 letters of the variable word
    * ```middle_word``` should contain the value of the variable word without the first and last letters

```
guillaume@ubuntu:~/py/$ python3 1-edges.py
First 3 letters: Hol
Last 2 letters: on
Middle word: olberto
guillaume@ubuntu:~/py/$ wc -l 1-edges.py
8 1-edges.py
guillaume@ubuntu:~/py/$
```

2. Positive anything is better than negative nothing
This program will assign a random signed number to the variable number each time it is executed. Complete the source code in order to print whether the number stored in the variable number is positive or negative.

    * You can find the source code 2-pon.py
    * The variable number will store a different value every time you will run this program
    * You don’t have to understand what import, random. randint do. Please do not touch this code
    * The output of the program should be:
    * The number, followed by
        * if the number is greater than 0: ```is positive```
        * if the number is 0: ```is zero```
        * if the number is less than 0: ```is negative```
    * followed by a new line
```
guillaume@ubuntu:~/$ python3 2-positive_or_negative.py
-4 is negative
guillaume@ubuntu:~/$ python3 2-positive_or_negative.py
0 is zero
guillaume@ubuntu:~/$ python3 2-positive_or_negative.py
-3 is negative
guillaume@ubuntu:~/$ python3 2-positive_or_negative.py
-10 is negative
guillaume@ubuntu:~/$ python3 2-positive_or_negative.py
10 is positive
guillaume@ubuntu:~/$ python3 2-positive_or_negative.py
-5 is negative
guillaume@ubuntu:~/$ python3 2-positive_or_negative.py
6 is positive
guillaume@ubuntu:~/$ python3 2-positive_or_negative.py
7 is positive
guillaume@ubuntu:~/$ python3 2-positive_or_negative.py
5 is positive
guillaume@ubuntu:~/$
```

3. The last digit
This program will assign a random signed number to the variable number each time it is executed. Complete the source code in order to print the last digit of the number stored in the variable number.
    * You can find the source code 3-last_digit.py
    * The variable ```number``` will store a different value every time you will run this program
    * You don’t have to understand what ```import```, ```random.randint``` do. Please do not touch this code. This line should not change: ```number = random.randint(-10000, 10000)```
    * The output of the program should be:
        * The string ```Last digit of```, followed by
        * the number, followed by
        * the string ```is```, followed by the last digit of ```number```, followed by
            * if the last digit is greater than 5: the string ```and is greater than 5```
            * if the last digit is 0: the string ```and is 0```
            * if the last digit is less than 6 and not 0: the string ```and is less than 6 and not 0```
    * followed by a new line
```
guillaume@ubuntu:~/$ python3 3-last_digit.py
Last digit of 4205 is 5 and is less than 6 and not 0
guillaume@ubuntu:~/$ python3 3-last_digit.py
Last digit of -626 is -6 and is less than 6 and not 0
guillaume@ubuntu:~/$ python3 3-last_digit.py
Last digit of 1144 is 4 and is less than 6 and not 0
guillaume@ubuntu:~/$ python3 3-last_digit.py
Last digit of -9200 is 0 and is 0
guillaume@ubuntu:~/$ python3 3-last_digit.py
Last digit of 5247 is 7 and is greater than 5
guillaume@ubuntu:~/$ python3 3-last_digit.py
Last digit of -9318 is -8 and is less than 6 and not 0
guillaume@ubuntu:~/$ python3 3-last_digit.py
Last digit of 3369 is 9 and is greater than 5
guillaume@ubuntu:~/$ python3 3-last_digit.py
Last digit of -5224 is -4 and is less than 6 and not 0
guillaume@ubuntu:~/$ python3 3-last_digit.py
Last digit of -4485 is -5 and is less than 6 and not 0
guillaume@ubuntu:~/$ python3 3-last_digit.py
Last digit of 3850 is 0 and is 0
guillaume@ubuntu:~/$ python3 3-last_digit.py
Last digit of 5169 is 9 and is greater than 5
guillaume@ubuntu:~/$
```