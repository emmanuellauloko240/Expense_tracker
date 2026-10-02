expenses = []

def expenses_tracker():

    total = 0
    while True:
        

        expense = input("Enter expense: ")
        amount = float(input("Enter amount: "))
        total += amount
        one_expense = {
            "item": expense
            "amount":amount
        }
        # expense + amount
        expenses.append(one_expense)
        another = input("Do you want another expenses? (yes/no): ")
        if another == "no" or another == "n":
            break
    # print(expenses)
    # print(f"Total cost spent: ₦{amount}")
    print(f"expense: {expense}")
    print(f"total expenses: ₦{total}")
        
expenses_tracker()


