"""
Problem: Given a string containing only square brackets, [], you must check whether the brackets are balanced or not.
The brackets are said to be balanced if, for every opening bracket, there is a closing bracket.You will write your
code in the check_balance() function, which returns True if the brackets are balanced and False if they are not.
For an empty string, the function will return True.
"""


def check_balance(brackets):
    check = 0
    if brackets:
        if brackets[0] == ']' or len(brackets) % 2 != 0:
            return False
        for bracket in brackets:
            if bracket == '[':
                check += 1

            elif bracket == ']':
                check -= 1

            if check < 0:
                break
        return check == 0
    else:
        return True


print(check_balance("[[]]]["))
