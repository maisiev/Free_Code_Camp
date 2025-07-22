
import tkinter as tk
from tkinter import messagebox

def add_expense(expenses, amount, category):
    expenses.append({'amount': amount, 'category': category})

def print_expenses(expenses):
    for expense in expenses:
        print(f'Amount: {expense["amount"]}, Category: {expense["category"]}')

def add_expense_button():
    amount = float(input('Enter amount: '))
    category = input('Enter category: ')
    add_expense(expenses, amount, category)
    messagebox.showinfo("Success", "Expense added successfully!")

    
root = tk.Tk()
root.title("Expense Tracker Application")
root.geometry("300x300")
root.configure(bg="pink")
button = tk.Button(root, text="Add an Expense", command=add_expense_button)
button.pack(pady=20)
button.configure(bg="blue", fg="black", activebackground="lightblue", highlightbackground="pink", font=("Courier New", 12, "bold"))

def list_all_expenses_button():
    print_expenses(expenses)
    messagebox.showinfo("Expenses", "Expenses listed in the console.")
button2 = tk.Button(root, text="List all Expenses", command=list_all_expenses_button)
button2.pack(pady=10)
button2.configure(bg="red", activebackground="red", highlightbackground="pink", font=("Courier New", 12, "bold"))
def show_total_expenses_button():
    total = sum(expense['amount'] for expense in expenses)
    messagebox.showinfo("Total Expenses", f"Total expenses: {total}")
    messagebox.showinfo("Expenses", "Here are all your expenses!")
button3 = tk.Button(root, text="Show Total Expenses", command=show_total_expenses_button)
button3.pack(pady=10)
def filter_expenses_by_category_button():
    category = input('Enter category to filter: ')
    filtered = [expense for expense in expenses if expense['category'] == category]
    for expense in filtered:
        print(f'Amount: {expense["amount"]}, Category: {expense["category"]}')
    messagebox.showinfo("Filtered Expenses", f"Filtered expenses listed in the console.")
def exit_button():
    root.destroy()
button4 = tk.Button(root, text="Filter Expenses by Category", command=filter_expenses_by_category_button)
button4.pack(pady=10)
button4.configure(bg="red", activebackground="red", highlightbackground="pink", font=("Courier New", 12, "bold"))

expenses = []

 

# Remove the duplicate `root.mainloop()` and fix button placements
# Ensure all buttons are properly configured and displayed

# Correct placement of the "Exit" button
button5 = tk.Button(root, text="Exit", command=exit_button)
button5.pack(pady=10)
button5.configure(bg="red", activebackground="red", highlightbackground="pink", font=("Courier New", 12, "bold"))

# Start the Tkinter event loop
root.mainloop()
