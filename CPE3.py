Python 3.12.1 (tags/v3.12.1:2305ca5, Dec  7 2023, 22:03:25) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
if firstName == "":
    print("Please enter something!\n")
else:
    print("You are now registered\n")

Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    if firstName == "":
NameError: name 'firstName' is not defined
firstName=input("What is your first name? ")
What is your first name? 



if firstName == "":
...     print("Please enter something!\n")
... else:
...     print("You are now registered\n")
... 
Please enter something!

>>> firstName=input("What is your first name? ")
What is your first name? Mark Daniel
>>> print(firstName)
Mark Daniel
>>> lastName=input("What is your last name? ")
What is your last name? Partoza
>>> print(lastName)
Partoza
>>> location=input("What is your address? ")
What is your address? Barangay Dagum, P-4, Calbayog City, Samar
>>> print(location)
Barangay Dagum, P-4, Calbayog City, Samar
>>> age=input("How old are you? ")
How old are you? 18
>>> age=int(input("How old are you? "))
How old are you? 18
>>> print("I am "+str(age)" years old")
SyntaxError: invalid syntax. Perhaps you forgot a comma?
>>> print("I am ", +str(age), " years old")
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    print("I am ", +str(age), " years old")
TypeError: bad operand type for unary +: 'str'
>>> age=int(input("How old are you? "))
How old are you? 18
>>> print("I am "+str(age)+" years old")
I am 18 years old
>>> print(firstName+"\n"+lastName+"\n"+location+"\n"+str(age)+" years old\n")
Mark Daniel
Partoza
Barangay Dagum, P-4, Calbayog City, Samar
18 years old

