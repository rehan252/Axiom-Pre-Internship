"""
This document provide some builtin function in Python.
Also lambda function as Anonymous function
"""

string = "This world is full of opportunities"
string.find("world")  # return index of found string
string.replace("world", "universe")  # first string is what to find , second is to replace with
len(string)  # return length of string
id(string)  # return memory address of variable where it's stored in system
my_list = [5, 6, 0, 4, 722, 17, 2, 1]
my_list.sort()  # sort string in to ascending order


# There are so many built-in functions we can use


# Lambda function also known as Anonymous function

def product_of_two(num):
    return num * 2


# we can convert this function into one line expression


num_square = lambda num: num * 2
print(num_square(12))

data = lambda num: "Number can't be less than 1" if num < 1 else num*2
print(data(15))

