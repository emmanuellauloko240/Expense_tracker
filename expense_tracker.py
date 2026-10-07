def get_total():


    # expenses = []

    total = 0

    # description = input("What did you spend on? ")
    # amount = float(input("How much did you spend? "))
    # new_expenses = {
    #     "description": description,
    #     "amount": amount
    # }

    # expenses.append(new_expenses)

    for expense in expenses:
        total += expense["amount"]
    return total
    # print(f"Total spent: {total}")

    # print(expenses)