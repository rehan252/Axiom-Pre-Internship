"""
This document provide brief description of operators use in Python.
Arithmetic, Logical, e.t.c
"""

# Arithmetic Operators (listed below from lower to higher Precedent)
print(18 - 12)  # Subtraction operation, result will be 6
print(10 + 12)  # Addition operation, result will be 32
print(14.5 // 3)  # Floor Division operation, result will be 4.0
print(10 / 12)  # Division operation, result will be 120
print(10 * 12)  # Multiplication operation, result will be 120
print(14 % 3)  # Modulus operation (provide remainder), result will be 2
print(2 ** 3)  # Exponent (power) operation, result will be 8
print((2+3)*3)  # Parentheses Precedent Operation, result will be 15, 2+3 will execute first

print('\n\n')  # for new lines
# Comparison Operators use for conditional structure
print(2 > 3)  # check is 2 greater than 3. will print False
print(2 < 3)  # check is 2 less than 3. will print True
print(3 >= 3)  # check is 3 greater than or equal to 3. will print True
print(3 <= 3)  # check is 3 less than or equal to 3. will print True
print(3 == 3)  # check is 3 equal to 3. will print True
print(3 is 3)  # check is 3 equal to 3 (work like ==). will print True
print(3 is not 3)  # check is 3 not equal to 3 (work like not ==). will print False
print(10 + 2 == 6 + 6)  # can also use arithmetic operations with logical. Will print True

print('\n\n')  # for new lines

# Assignment Operators -  use to assign values to variables as listed below
data = 125  # Assign integer 125 to variable data
data += 5  # This is equivalent to data=data+5, add 5 in data and then re-assign value to data - 130
data -= 5  # This is equivalent to data=data-5, subtract 5 from data and then re-assign value to data - 120
data *= 2  # This is equivalent to data=data*2, multiply 2 to data and then re-assign value to data - 250
data /= 5  # This is equivalent to data=data/5, divide data with 5 and then re-assign value to data - 25
data //= 5  # This is equivalent to data=data//5, floor divide data with 5 and then re-assign value to data - 25.0
data **= 2  # This is equivalent to data=data**2, take exponent of power 2 of data and then re-assign value to data -
# 15625
data %= 5  # This is equivalent to data=data%5, take modulus of data with 5 and then re-assign value to data - 0
data %= 5  # This is equivalent to data=data%5, take modulus of data with 5 and then re-assign value to data - 0

print('\n\n')  # for new lines

# Logical Operators -  AND, OR operators
print((2 > 3) and (3 == 3))  # check if 2 greater than 3 AND 3 is equal to 3, both cond. needs to be true - False
print((2 > 3) or (3 == 3))  # check if 2 greater than 3 OR 3 is equal to 3, one cond. needs to be true - True
print(not False)  # return True if condition or operand is False - True

print('\n\n')  # for new lines

# Bitwise Operators -  to perform bit-related operations on values
num1 = 10  # Binary value = 01010
num2 = 20  # Binary Value = 10100

print(num1 & num2)  # perform AND between both binary (= num1*num2) - 00000
print(num1 | num2)  # perform OR between both binary (= num1+num2) - 11110
print(num1 << 3)  # move 3steps bitwise to the left - 0101 0000
print(num2 >> 3)  # move 3steps bitwise to the right - 0010
