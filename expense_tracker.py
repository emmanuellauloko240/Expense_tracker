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
def view_expense():
    for expense in expenses:
        print(f"description: {expense['description']}, amount: {expense['amount']}")

while True:
    choice = (input("Menu: 1. Add Expense, 2. View Expenses, 3. Show-Total, 4. Exit: "))

    if choice == "1":
        add_expense()
    elif choice == "2":
        view_expense()
    elif choice == "3":
        print (f"Total spent:  {get_total()}")
    elif choice == "4":
        print("Goodbye")
        break
    else:
        print("invalid choice message🙂")


