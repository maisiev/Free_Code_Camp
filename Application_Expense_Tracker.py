import tkinter as tk
from tkinter import messagebox

# Initialize the main application window
root = tk.Tk()
root.title("Expense Tracker Application")
root.geometry("300x400")
root.configure(bg="pink")
label = tk.Label(root, text='TIME TO BUDGET!!!', bg="pink", font=("Courier New", 15, "bold")).pack(pady=5)

# Initialize the expenses list
expenses = []

def add_expense_button():
    def open_new_window():
        # Create a new window for adding expenses
        new_window = tk.Toplevel(root)
        new_window.title("Add Expense")
        new_window.geometry("300x200")
        new_window.configure(bg="lightblue")
        
        # Create input fields for expense amount and category
        tk.Label(new_window, text="Enter Expense Amount", bg="lightblue", font=("Courier New", 12)).pack(pady=10)
        amount_entry = tk.Entry(new_window, width=30)
        amount_entry.pack(pady=5)
        
        tk.Label(new_window, text="Enter Expense Category", bg="lightblue", font=("Courier New", 12)).pack(pady=10)
        category_entry = tk.Entry(new_window, width=30)
        category_entry.pack(pady=5)
        
        # Submit button to add expense
        def submit_expense():
            try:
                # Retrieve user input from the Entry widgets
                amount = float(amount_entry.get())
                category = category_entry.get()
                
                # Add the expense to the list
                add_expense(expenses, amount, category)
                
                # Show success message and close the window
                messagebox.showinfo("Expense", "Expense Added!")
                new_window.destroy()
            except ValueError:
                # Handle invalid input for the amount
                messagebox.showerror("Error", "Invalid amount entered!")
        
        tk.Button(new_window, text="Submit", command=submit_expense, bg="green", highlightbackground="lightblue", font=("Courier New", 10)).pack(pady=10)
    
    # Define the add_expense function
    def add_expense(expenses, amount, category):
        expenses.append({'amount': amount, 'category': category})

    # Open the new window
    open_new_window()

# Add a button to open the expense window
button = tk.Button(root, text="Add an Expense", command=add_expense_button, bg="red", activebackground="red", highlightbackground="pink", font=("Courier New", 12, "bold"))
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
