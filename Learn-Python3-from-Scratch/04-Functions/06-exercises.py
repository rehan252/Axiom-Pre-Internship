"""
Problem 1: In this exercise, you must implement the rep_cat function.
You are given two integers, x and y, as arguments. You must convert them
into strings. The string value of x must be repeated 10 times and the string
value of y must be repeated 5 times.
"""


def rep_cat(x, y):
    return (str(x) * 10) + (str(y) * 5)


print(rep_cat(4, 8))


"""
In this challenge, you must implement the factorial() function. It takes an integer as a parameter and 
calculates its factorial. The factorial of a number, n, is its product with all the integers between 0 and n.
factorial(n) = n*(n-1)*(n-2)*....*1
"""


def factorial(num):
    if num < 0:
        return -1

    elif num == 1 or num == 1:
        return 1

    else:
        return num * factorial(num - 1)


print(factorial(5))
