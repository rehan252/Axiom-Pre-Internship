"""
This doc provide brief details about functions in Python and their
scope.
"""


def upper_case(string):
    return string.upper()


print(upper_case('hello'))


def print_num(num1, num2):
    if num1 > num2:
        return num1
    else:
        return num2


print(print_num(10, 541))


# Function scope variable is either function scope or global scope
data = "Hello"


def print_data():
    data = 21
    print(data)


print(data)  # This will print "Hello" as it's global scope
print_data()  # This will print 21 as function levelvariable doesn't change global variable

# to change global variable inside function we use global with variable


def print_global():
    global data
    data = 20
    print(data)


print_global()  # This will print 20 as we override global var using global
