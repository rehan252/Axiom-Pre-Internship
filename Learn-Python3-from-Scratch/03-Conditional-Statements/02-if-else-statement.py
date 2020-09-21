"""
This doc is used to understand the conditional if-else structure
in Python. Syntax:
if condition:
    code execute
else:
    code execute
"""
# lets convert below code into if-else statement
num = 6
if num > 2:
    print(2)
if num < 8:
    num = 10
    print(num)

# if-else statement

if num < 8:
    num = 10
    print(num)
else:
    print(2)

# Conditional Expression
print(2) if num > 2 else print(num)


# if-elif-else statement - example using bank debit

balance = 1000
debit = int(input("Enter debit amount"))
if debit < 500:
    print("Can't debit less than 500")
elif debit > balance:
    print("Debited amount is greater than current balance")
else:
    balance -= debit
    print("{} amount is debited from your account".format(debit))

