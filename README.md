# Expense Tracker

A command-line Python program for tracking spending. Add expenses with a description and an amount, view them all, and see the running total. Everything is saved to a file, so your data is still there next time.

## How to Run

1. Make sure you have Python 3 installed.
2. Clone this repository:
```bash
   git clone https://github.com/emmanuellauloko240/Expense_tracker.git
```
3. Navigate into the project folder:
```bash
   cd Expense_tracker
```
4. Run the program:
```bash
   python3 expense_tracker.py
```

## Features

- Add an expense with a description and an amount (decimals supported)
- View all expenses in a readable list
- Show the total amount spent
- Automatically saves expenses to `expenses.json` and loads them on startup
- Menu-driven interface that keeps running until you choose Exit

## What I Learned

Building this project helped me understand:

- Storing records as dictionaries inside a list
- Using `float()` to handle money amounts with decimals
- Writing functions that `return` a value (`get_total`)
- Variable scope, and why a variable inside a function isn't visible outside it
- Looping through a list to calculate a sum
- Building a menu with a `while` loop and `if`/`elif`/`else`
- Saving and loading data with the `json` module
- Reading error messages and tracing indentation and typo bugs