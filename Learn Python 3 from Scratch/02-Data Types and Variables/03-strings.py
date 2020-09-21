"""
This document provide brief description strings in Python
"""

print("Hello World..")  # Double quotes
print('Hello World...')  # Single quote
print("")  # empty string

# To find length of string use function len()
print(len('Python is best'))

# We can also find character in string using Indexing
string = "Python is best"
print(string[0])  # will print 'P' first character in string
print(string[8])  # will print 's' ninth character in string

# Reverse Indexing
print(string[-1])  # will print last index value 't'
print(string[-3])  # will third last character in string 'e'

"""
We can use Slicing on string to select range of elements from string.
Syntax: string[start:end] which means select from start (inclusive) to end(exclusive)
"""
slicer = "Batman Robin Joker"
# Index : 012345678901234567  (representing indexes after 9 it's 10, 11 so on.)

print(slicer[7:12])  # will print 'Robin' because i select start from 7 to 12 but don't include 12
print(slicer[::-1])  # select all but in reverse order due to -1 at end (rekoJ niboR namtaB)

# Step slicing - default step is 1 but we can specify
print(slicer[2:8:2])  # will print character at index 2 and then after 2 steps character at inedx 4 and then 6
# will print 'ta '

# Partial Slicing
print(slicer[:4])  # will print from start to index 3
print(slicer[4:])  # will print from index 4 to end

# String Operations - perform different operations on string
print('a' < 'b')  # string comparison check if 'a' has a smaller Unicode value
print(slicer + ' Harley')  # concatenate the string slicer
print('Ha' * 5)  # print 'Ha' 5 times
print('in' in slicer)  # check 'in' is in slicer string

