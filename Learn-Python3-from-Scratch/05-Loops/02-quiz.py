"""
This doc. contains quiz questions related to for loop and while loop


Q1: Have a look at the for loop below:
    string_list = ["Anakin", "Luke", "Rey", "Leia", "Vader"]
    for s in string_list:
        if len(s) < 5:
            print(len(s))

Ans:    4
        3
        4

Q2: In the following code, how would we replace the for loop with a while loop?
    string_list = ["Anakin", "Luke", "Rey", "Leia", "Vader"]
    for s in string_list:
        if len(s) < 5:
            print(len(s))

Ans:    string_list = ["Anakin", "Luke", "Rey", "Leia", "Vader"]
        i = 0
        while i < len(string_list):
            if len(string_list[i]) < 5:
                print(len(string_list[i]))
            i += 1

Q3: A while loop runs as long as its condition holds True.
Ans: True

Q4: What is the purpose of the break statement?
Ans: It ends the loop.
"""