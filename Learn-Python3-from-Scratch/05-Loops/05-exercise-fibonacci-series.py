"""
Problem: As we saw earlier, the Fibonacci sequence is a series of numbers where every number is the sum of the
two numbers before it. The first two numbers are 0 and 1: 0 1 1 2 3 5 8 13 You must write the fib()
function which takes in a positive integer, n, and returns the n-th Fibonacci number. However, instead
of using recursion, your function must use any of the loops.
"""


def fib(num):
    first = 0
    second = 1
    if num == 0:
        return False
    elif num == 1:
        return first
    elif num == 2:
        return second
    while num > 2:
        total = first + second
        first = second  # shuffling values
        second = total
        num -= 1
    return total


print(fib(8))
