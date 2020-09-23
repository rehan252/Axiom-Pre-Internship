"""
In this doc, we will explore the Python Standard Library.
Generally, a module contains functions related to a particular aspect of programming.
This makes things easy because we know which part of our program requires which module.
"""

import datetime
import random
from math import factorial as ft, log
from heapq import heappush as push, heappop as pop

print(datetime.date.today())
print(datetime.datetime.now())
print(datetime.datetime.now().strftime('%m/%d/%Y, %H:%M:%S'))
print(datetime.datetime.now().strftime('%Y'))  # will print year

print(ft(4))
print(log(10))

"""
The heapq module allows us to create the heap data structure. A heap is a binary
tree which always stores a special value at the top (root). A minheap stores the 
smallest value at the top and a maxheap stores the largest value at the top.
"""

heap = []
push(heap, 74)
push(heap, 10)
push(heap, 5)
push(heap, 12.001)

print(heap)

pop(heap)
print(heap)

"""
Random Module: to generate random numbers
"""
print(random.random())
print(random.uniform(3, 50))
