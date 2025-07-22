import tkinter as tk
from tkinter import messagebox

def add_expense_button():
    tk.Label(text="Add Expense Window", font=("Courier New", 12))
root = tk.Tk()
root.title("Expense Tracker Application")
root.geometry("300x300")
root.configure(bg="pink")
button = tk.Button(root, text="Add an Expense", command=add_expense_button)
button.configure(bg="red", activebackground="red", highlightbackground="pink", font=("Courier New", 12, "bold"))



def list_all_expenses_button():
    messagebox.showinfo("Expenses", "Expenses listed in the console.")
button3 = tk.Button(root, text="Exit", command=list_all_expenses_button)
button3.pack(pady=10)
button3.configure(bg="red", activebackground="red", highlightbackground="pink", font=("Courier New", 12, "bold"))


def show_total_expenses_button():
    messagebox.showinfo("Expenses", "Expenses listed in the console.")
button3 = tk.Button(root, text="Exit", command=show_total_expenses_button)
button3.pack(pady=10)
button3.configure(bg="red", activebackground="red", highlightbackground="pink", font=("Courier New", 12, "bold"))


def filter_expenses_by_category_button():
    messagebox.showinfo("Expenses", "Here are all your expenses!")
button4 = tk.Button(root, text="Filter Expenses by Category", command=filter_expenses_by_category_button)
button4.pack(pady=10)
button4.configure(bg="red", activebackground="red", highlightbackground="pink", font=("Courier New", 12, "bold"))

def exit_button():
    messagebox.showinfo("Expenses", "Here are all your expenses!")
button5 = tk.Button(root, text="Exit", command=exit_button)
button5.pack(pady=10)
button5.configure(bg="red", activebackground="red", highlightbackground="pink", font=("Courier New", 12, "bold"))






root.mainloop()




# This script creates a simple GUI application using Tkinter in Python.
# It displays a button that, when clicked, shows a message box with a greeting.
# The application window is set to a size of 300x200 pixels.
# The button is centered in the window with some padding for better appearance.
# The script is ready to run and will display a welcome message when the button is clicked.





    

