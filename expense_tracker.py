expenses = []


def get_total():
    total = 0
    for expense in expenses:
        total += expense["amount"]
    return total


def add_expense():
    description = input("What did you spend on? ")
    amount = float(input("How much did you spend? "))

    new_expense = {
        "description": description,
        "amount": amount
    }

    expenses.append(new_expense)
    print("Success........")


add_expense()
add_expense()
print(f"Total spent: {get_total()}")
print(expenses)