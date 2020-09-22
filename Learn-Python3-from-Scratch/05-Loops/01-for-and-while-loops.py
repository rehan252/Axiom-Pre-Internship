"""
In this doc we'll go through for and while loop in Python
for loop syntax: for i in range(start,end,step) e.g.
"""

for i in range(2, 10):
    if i % 2 == 0:
        print(i)

# we can recreate above using step attribute

for i in range(2, 10, 2):
    print(i)

# Using List
loop_list = [2, "Hello", "Fella", 5, "6", 12.7, "World", 9, 10]

length = len(loop_list)
for i in loop_list:
    print(i)  # print each element of list

# Nested For Loop
found = False
list_data = [2, 5, 4, 8, 7, 2, 9]

for l1 in list_data:
    for l2 in list_data:
        if l1 % l2 != 0:
            found = True
            print(l1, l2)
            break
    if found:
        break

# continue statement
# print data which is not divisible by 3 and 4
for d in list_data:
    if d % 3 == 0 or d%4 == 0:
        continue
    print(d)


"""
While loop unlike for loop range in while loop we don't need to give range for loop.
The loop while continue to iterate until certain while condition gets failed
"""
iterator = 5
while iterator > 0:
    print("Python is Best")
    iterator -= 1

