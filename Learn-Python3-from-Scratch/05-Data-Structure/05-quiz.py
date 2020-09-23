"""
Quiz for Data Structure

Q1: Which of the following sets of properties is true for a list?
Ans:    Ordered
        Mutable
        Indexed

Q2: For a given data structure, ds, what is the correct way of calculating its length?
Ans: len(ds)

Q3: In a dictionary, key-value pairs are indexed by _____.
Ans: Keys

Q4: A set can contain a tuple, but not a list.
Ans: True

Q5: What will be the value of entry at the end of this code?
    traffic_light = {"Green": "Go", "Yellow": "Wait", "Red": "Stop"}
    entry = traffic_light.popitem()

Ans: ("Red", "Stop")

Q6: An empty set can be made using ______.
Ans: set()

Q7: What is the correct list comprehension for the following code?
    string_list = ["Anakin", "Luke", "Rey", "Leia", "Vader"]
    result = []
    for s in string_list:
        if len(s) < 5:
            result.append(len(s))

Ans: string_list = ["Anakin", "Luke", "Rey", "Leia", "Vader"]
result = [len(s) for s in string_list if len(s) < 5]
"""