# Expense Tracker

A command-line Python program for tracking spending. Add expenses with a description and an amount, view them all, and see the running total.

## How to Run

1. Make sure you have Python 3 installed.
2. Clone this repository:
`````bash
   git clone https://github.com/emmanuellauloko240/Expense_tracker.git
`````
3. Navigate into the project folder:
`````bash
   cd Expense_tracker
`````
4. Run the program:
`````bash
   python3 expense_tracker.py
`````

## Features

- Add an expense with a description and an amount (decimals supported)
- View all expenses in a readable list
- Show the total amount spent
- Menu-driven interface that keeps running until you choose Exit

## Coming Next

- Save expenses to a file so they persist between sessions

## What I Learned

Building this project helped me understand:

- Storing records as dictionaries inside a list
- Using `float()` to handle money amounts with decimals
- Writing functions that `return` a value (`get_total`)
- Variable scope, and why a variable inside a function isn't visible outside it
- Looping through a list to calculate a sum
- Building a menu with a `while` loop and `if`/`elif`/`else`
- Reading error messages and tracing indentation bugs
`````
`````

Before you save it, check two things:

1. **The clone URL.** Make sure `Expense_tracker` matches your actual GitHub repo name, including capital letters.
2. **The tracker filename.** `expense_tracker.py` should match your file exactly.

Then save, commit, and push everything:

`````bash
git add README.md expense_tracker.py
git commit -m "Add expense menu and README"
git push
`````

