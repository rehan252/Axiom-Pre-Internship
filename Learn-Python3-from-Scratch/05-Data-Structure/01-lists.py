"""
This doc provide detailed overview of List operations and
list Comprehension e.t.c.
"""

list1 = ["hello", 2, 0.8, [5, "point", 'boil'], 100]

print(list1[2])  # print 0.8
print(list1[0][1])  # print 'e' from hello
print(list1[3])  # will print [5, "point", 'boil']
print(list1[3][1])  # will print 'point' from [5, "point", 'boil']

# OPERATIONS
list1.pop()  # remove last element from list
print(list1)

list1.append('wire')  # add element at the end of array
list1.insert(2, 'inserted')  # add element at specified index
print(list1.index('inserted'))  # find the index of element in the lesson
print(list1)

print("point" in list1)  # return True if elements found in list else False

"""
List Comprehension, just like lambda function we can perform one line function inside list.
e.g. for loops and if else we can use inside list. it always return list
"""

# Transpose of 2d list using loop

lists = [[1, 2, 3],
         [4, 5, 6],
         [7, 8, 9]]
transpose = []
for i in range(len(lists[0])):
    t_row = []
    for r in lists:
        t_row.append(r[i])
    transpose.append(t_row)
print(transpose)

# Let's recreate above function using list Comprehension
# [expression for item in list], Inner loop will be use as Expression for outer loop
transpose = [[r[i] for r in lists] for i in range(len(lists))]
print(transpose)

