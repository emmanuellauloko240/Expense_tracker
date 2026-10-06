expenses = []

def expenses_tracker():

    total = 0
    while True:

        expense = input("Enter expense: ")
        while True:
            try:
                amount = float(input("Enter amount: "))
            except ValueError:
                print("Enter a valid input..")
                continue 
            total += amount
            one_expense = {"item": expense, "amount":amount}
            # expense + amount
            expenses.append(one_expense)
            another = input("Do you want another expenses? (yes/no): ")
            if another == "no" or another == "n":
                break
        for expense in expenses:
            item = expense["item"]
            amount = expense["amount"]
            print(f"{item}: ₦{amount:.2f}")
        # print(expenses)
        # print(f"Total cost spent: ₦{amount}")
        # print(f"expense: {expense}")
        # print(f"total expenses: ₦{total.2f}")

        print(f"total expenses: ₦{total}")
            
    expenses_tracker()


