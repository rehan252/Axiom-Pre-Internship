"""
In This doc we are going to pass functions as arguments to other
let's start by creating a calculator
"""

# creating list of operations to perform


def add(num1, num2): return num1 + num2


def subtract(num1, num2): return num1 - num2


def multiply(num1, num2): return num1 * num2


def divide(num1, num2): return num1 / num2


def modulus(num1, num2): return num1 % num2


def calculator(opt, num1, num2):  # passing 'opt' argument as function
    return opt(num1, num2)


print(calculator(multiply, 2, 4))


# Using lambda and map function

list1 = [2, 7, 4, 9, 7]
list2 = [3, 6, 1, 9, 7]
op = [add, subtract, multiply, divide, modulus]
small_calc = list(map(lambda op , a, b: op(a, b), op, list1, list2))  # perform each operation against each element of list
print(small_calc)


"""To get Conditional result we use 'filter()' work same as 'if' condition and returns
   a filtered new list, Syntax:
   list(map(lambda Argument: Condition/Expression, list))"""

lists = [2, 5, 3, 7, 10, 4, 18, 67, 122]
filtered = list(filter(lambda x: x%3 == 0, lists))
print("List of Numbers Divisible by 3: {}".format(filtered))
