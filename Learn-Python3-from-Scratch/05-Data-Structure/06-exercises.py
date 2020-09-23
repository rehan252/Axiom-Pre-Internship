"""
Problem 1: You are given a list called my_list. Using this list, you must create a tuple called
 my_tuple. The tuple will contain the list’s first element, last element, and the length of the list,
in that same order. Sample Input #
my_list = [34, 82.6, "Darth Vader", 17, "Hannibal"]
"""
my_list = [34, 82.6, "Darth Vader", 17, "Hannibal"]
data = (my_list[0], my_list[-1], len(my_list))
print(data)

"""
Problem 2 - Kth Maximum Integer in a List: Given a list of integers and a number k, find the kth maximum element 
in the list. The element will be stored in the kth_max variable.
"""


def find_kth(numbers, k):
    numbers.sort()
    return numbers[-k]


print(find_kth([40, 35, 82, 14, 22, 66, 53], 6))

"""
Problem 3 - Highs and Lows: You must implement the count_low_high() function. 
Its parameter is a list of numbers. If a number is greater than 50 or divisible 
by 3, it will count as a high. If these conditions are not met, the number is considered a low.
At the end of the function, you must return a list that contains the number of lows and highs, 
in that order. In case the list is empty, you may return None.
Sample Input #
num_list = [20, 9, 51, 81, 50, 42, 77]
"""


def count_low_high(numbers):
    high = len(list(filter(lambda n: n % 3 == 0 or n > 50, numbers)))
    low = len(list(filter(lambda n: n % 3 != 0 and not n > 50, numbers)))
    return [low, high]


print(count_low_high([20, 9, 51, 81, 50, 42, 77]))
