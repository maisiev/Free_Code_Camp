import tkinter as tk
from tkinter import messagebox


def add_expense_button():
    messagebox.showinfo("Expenses", "Expenses listed in the console.")
root = tk.Tk()
root.title("Expense Tracker Application")
root.geometry("300x350")
root.configure(bg="pink")
label = tk.Label(root, text='TIME TO BUDGET!!!', bg="pink", font=("Courier New", 15, "bold")).pack()

button = tk.Button(root, text="Add an Expense", command=add_expense_button)
button.configure(bg="red", activebackground="red", highlightbackground="pink", font=("Courier New", 12, "bold"))
button.pack(pady=20)


def list_all_expenses_button():
    messagebox.showinfo("Expenses", "Expenses listed in the console.")
button2 = tk.Button(root, text="List all Expenses", command=list_all_expenses_button)
button2.pack(pady=20)
button2.configure(bg="red", activebackground="red", highlightbackground="pink", font=("Courier New", 12, "bold"))


def show_total_expenses_button():
    messagebox.showinfo("Expenses", "Expenses listed in the console.")
button3 = tk.Button(root, text="Show Total Expenses", command=show_total_expenses_button)
button3.configure(bg="red", activebackground="red", highlightbackground="pink", font=("Courier New", 12, "bold"))
button3.pack(pady=20)
button3.configure(bg="red", activebackground="red", highlightbackground="pink", font=("Courier New", 12, "bold"))


def filter_expenses_by_category_button():
    messagebox.showinfo("Expenses", "Here are all your expenses!")
button4 = tk.Button(root, text="Filter Expenses by Category", command=filter_expenses_by_category_button)
button4.pack(pady=20)
button4.configure(bg="red", activebackground="red", highlightbackground="pink", font=("Courier New", 12, "bold"))

def exit_button():
    messagebox.showinfo("Expenses", "Bye!")
    root.destroy()
button5 = tk.Button(root, text="Exit", command=exit_button)
button5.pack(pady=20)
button5.configure(bg="red", activebackground="red", highlightbackground="pink", font=("Courier New", 12, "bold"))



root.mainloop()
