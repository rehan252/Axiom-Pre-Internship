"""
Problem 1:
Write a Python class named Rectangle constructed by a length and width and a method which will
compute the area of a rectangle
"""


class Rectangle():
    def __init__(self, l, w):
        self.length = l
        self.width = w

    def area(self):
        return self.length*self.width


rect = Rectangle(12, 10)
print(rect.area())