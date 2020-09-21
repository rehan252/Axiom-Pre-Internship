"""
This doc is used to understand the conditional if structure
in Python. Syntax:
if condition:
    code execute
"""

# Single if statement
num = 5
if num < 6:  # as condition will be true
    print(num)  # this print 5


# Multiple if statement
if num > 2:
    print(2)
if num < 8:
    num = 10
    print(num)

# Nested if statement
if num < 10:
    if num > 2:
        num = 12
        print(num)

