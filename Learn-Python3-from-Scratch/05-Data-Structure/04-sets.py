"""
This doc provide detailed overview of sets in Python.
These are basically unordered collection of data items. Can't contain repeated values
Mutable data structures like lists or dictionaries can’t be added to a set.
 However, adding a tuple is perfectly fine.
"""

# Syntax:
data_set = set()
data_set.add(5)
print(data_set)
data_set.update([True, 12, (5, "point", 'boil'), 100])
print(data_set)

# print integers only from set
for sets in data_set:
    if isinstance(sets, int):
        print(sets)

# Union and Intersection of sets
set_A = {1, 2, 3, 4}
set_B = {2, 8, 4, 16}

print(set_A.union(set_B))
print(set_A.intersection(set_B))

print(set_B & set_A)
print(set_B | set_A)

# Difference
print(set_A - set_B)
print(set_B.difference(set_A))

