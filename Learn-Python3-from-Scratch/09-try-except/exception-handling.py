"""
In this doc. we'll see how to handle exceptions in your code.
The try block lets you test a block of code for errors.
The except block lets you handle the error.
The finally block lets you execute code, regardless of the result of the try- and except blocks.
"""


# we know dividing number on zero will give error
try:
    2/0
except ZeroDivisionError:
    print("Number can't be divide by zero")

# print(2/0)

try:
    2/0
except ZeroDivisionError:
    print("Number can't be divide by zero")


# we can use finally if want something to must run at the end even if exception happened

try:
    2/0
except ZeroDivisionError:
    print("Number can't be divide by zero")
finally:
    print('Code executed...')

# if x is not defined in we'll define in exception and then we'll add 10 in our var whether exception happened or not
try:
    print(x)
except:
    x = 10
finally:
    print(x+10)


