"""
In this Doc we'll cover all details about classes in Python.
Class Inheritance e.t.c.
"""


# start by creating a simple example of Person


class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age


p1 = Person("David", 25)
print(p1.name)

# let's create a new class name Teacher and inherit it from person as every teacher must be person


class Teacher(Person):
    pass


t1 = Teacher("Rehan", 24)
print(t1.name)
print(t1.age)  # it's inherit properties of Person object

