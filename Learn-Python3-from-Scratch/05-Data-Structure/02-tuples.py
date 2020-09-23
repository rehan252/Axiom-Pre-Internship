"""
This doc provide detailed overview of tuples.
TUPLES : are just ordered list. main difference is tuples are immutable. we can't
change or update tuple
"""

data = (1, 3, 4, 6, 9, 22, 100)
print(data[1:4])  # slicing

# we can also use tricks to sort list using tuple
list1 = [101, 3, 124, 0.6, 9, 22, 10]
list1 = list(tuple(list1))
print(list1)

# merging tuples and converting list into tuple
tup = data + tuple(list1)
