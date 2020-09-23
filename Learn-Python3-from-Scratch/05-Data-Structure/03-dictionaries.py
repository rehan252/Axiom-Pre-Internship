"""
This doc provide detailed overview of dictionaries in Python.
These are basically key, values pairs in which keys are immutable and values can be both
"""

# syntax:
dict_data = dict()
# or, dict_data = {}

# create dict graphic card model with manufacturer
graphics = {'Nividia': 'GTX 1080', 'AMD': 'Redeon 980', 'Intel': 'HD Graphic 620'}

print(graphics['Intel'])  # print value against it

graphics['Asus'] = 'GeForce RTX™ 2080'  # adding new element in dict
graphics['AMD'] = 'Radeon MX-750'  # updating dic
print(graphics)

del graphics['Intel']  # delete intel from dict
print(graphics)

print('Asus' in graphics)  # check if key exists

# Dictionary comprehension
myDict = {x: x**2 for x in [1, 2, 3, 4, 5]}
print(myDict)







