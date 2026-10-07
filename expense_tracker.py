expenses = []

description = input("What did you spend on? ")
amount = input("How much did you spend? ")

new_expenses = {
    "description": description,
    "amount": amount
}
expenses.append(new_expenses)

print(expenses)