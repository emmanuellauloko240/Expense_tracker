import json


def save_expenses():
    with open("expenses.json", "w") as file:
        json.dump(expenses, file)


def load_expenses():
    try:
        with open("expenses.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []


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


def view_expenses():
    for expense in expenses:
        print(f"description: {expense['description']}, amount: {expense['amount']}")


expenses = load_expenses()

while True:
    choice = input("Menu: 1. Add Expense, 2. View Expenses, 3. Show-Total, 4. Exit: ")

    if choice == "1":
        add_expense()
        save_expenses()
    elif choice == "2":
        view_expenses()
    elif choice == "3":
        print(f"Total spent: {get_total()}")
    elif choice == "4":
        print("Goodbye")
        break
    else:
        print("Invalid choice, try again.")