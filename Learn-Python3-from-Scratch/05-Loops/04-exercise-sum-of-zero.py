"""
Problem: You must implement the check_sum() function which takes in a list and
returns True if the sum of two numbers in the list is zero. If no such pair exists, return False.
Use For or While Loop
"""


def check_sum(data):
    for d1 in data:
        for d2 in data:
            if d1 + d2 == 0:
                return d1, d2
    return False


print(check_sum([10, -14, 26, 5, -3, 13, -5]))

#  Using lambda function
