expenses = []

def get_total():

    total = 0

    for expense in expenses:

        total += expense["amount"]

    return total
description = input("What did you spend on? ")
amount = float(input("How much did you spend? "))
new_expenses = {
    "description": description,
    "amount": amount
}

expenses.append(new_expenses)

print(f"Total spent: {get_total()}")

print(expenses)
