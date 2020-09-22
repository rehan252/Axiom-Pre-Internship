"""
Recursion: when a function call itself during execution.
In this doc we'll go through detail overview of recursion
"""


def get_count(num):
    if num < 1:
        return 0
    get_count(num - 1)
    print(num)


get_count(5)  # it'll print 1 - 5 to as this func will call itself until it reaches 0

# Creating fibonacci series 0 1 1 2 ...


def fibonacci(num):
    if num == 1:
        return 0
    elif num == 2:
        return 1
    return fibonacci(num - 1) + fibonacci(num - 2)


print(fibonacci(8))
