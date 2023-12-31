# 5. Python - Classes and Objects

## 0. Square with size
Write a class ```Square``` that defines a square by:
* Private instance attribute: ```size```
* Instantiation with ```size``` (no type/value verification)
* You are not allowed to import any module
Why?
Why ```size``` is private attribute?
The size of a square is crucial for a square, many things depend of it (area computation, etc.), so you, as class builder, must control the type and value of this attribute. One way to have the control is to keep it privately. You will see in next tasks how to get, update and validate the size value.

## 1. Size validation
Write a class ```Square``` that defines a square by: (based on ```0-square.py```)
* Private instance attribute: ```size```
* Instantiation with optional ```size: def __init__(self, size=0):```
    * ```size``` must be an integer, otherwise raise a ```TypeError``` exception with the message ```size must be an integer```
    * if ```size``` is less than ```0```, raise a ```ValueError``` exception with the message ```size must be >= 0```
* You are not allowed to import any module

## 2. Area of a square
Write a class ``Square`` that defines a square by: (based on ```1-square.py```)
* Private instance attribute: ```size```
* Instantiation with optional ```size: def __init__(self, size=0):```
    * ```size``` must be an integer, otherwise raise a ```TypeError``` exception with the message ```size must be an integer```
    * if ```size``` is less than ```0```, raise a ```ValueError``` exception with the message ```size must be >= 0```
* Public instance method: ```def area(self):``` that returns the current square area
* You are not allowed to import any module

## 3. Access and update private attribute
Write a class ```Square``` that defines a square by: (based on ```2-square.py```)
* Private instance attribute: ```size```:
    * property ```def size(self):``` to retrieve it
    * property setter ```def size(self, value):``` to set it:
        * ```size``` must be an integer, otherwise raise a ```TypeError``` exception with the message ```size must be an integer```
        * if ```size``` is less than ```0```, raise a ```ValueError``` exception with the message ```size must be >= 0```
Instantiation with optional ```size: def __init__(self, size=0):```
Public instance method: ```def area(self):``` that returns the current square area
You are not allowed to import any module

**Why?**</br>
Why a getter and setter?
Reminder: ```size``` is a private attribute. We did that to make sure we control the type and value. Getter and setter methods are not 100% Python, but more OOP. With them, you will be able to validate the assignment of a private attribute and also define how getting the attribute value will be available from outside - by copy? by assignment? etc. Also, adding type/value validation in the setter will centralize the logic, since you will do it in only one place.

## 4. Printing a square
Write a class ```Square``` that defines a square by: (based on ```3-square.py```)
* Private instance attribute: ```size:```
    * property ```def size(self):``` to retrieve it
    * property setter ```def size(self, value):``` to set it:
        * ```size``` must be an integer, otherwise raise a ```TypeError``` exception with the message ```size must be an integer```
        * if ```size``` is less than ```0```, raise a ```ValueError``` exception with the message ```size must be >= 0```
* Instantiation with optional ```size: def __init__(self, size=0):```
* Public instance method: ```def area(self):``` that returns the current square area
* Public instance method: ```def my_print(self):``` that prints in stdout the square with the character ```#```:
    * if ```size``` is equal to 0, print an empty line
* You are not allowed to import any module
