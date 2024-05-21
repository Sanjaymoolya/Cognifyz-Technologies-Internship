import tkinter as tk
from tkinter import messagebox

def calculate():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        operator = operator_var.get()

        if operator == '+':
            result = num1 + num2
        elif operator == '-':
            result = num1 - num2
        elif operator == '*':
            result = num1 * num2
        elif operator == '/':
            if num2 == 0:
                raise ZeroDivisionError
            result = num1 / num2
        elif operator == '%':
            result = num1 % num2
        else:
            result = "Invalid operator"
        
        result_var.set(result)
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers")
    except ZeroDivisionError:
        messagebox.showerror("Math Error", "Division by zero is not allowed")

# Set up the main application window
root = tk.Tk()
root.title(" Cognifyz Basic Calculator")

# Create and place the input fields and labels
tk.Label(root, text="First Number:").grid(row=0, column=0, padx=10, pady=10)
entry1 = tk.Entry(root)
entry1.grid(row=0, column=1, padx=10, pady=10)

tk.Label(root, text="Operator:").grid(row=1, column=0, padx=10, pady=10)
operator_var = tk.StringVar()
operator_menu = tk.OptionMenu(root, operator_var, "+", "-", "*", "/", "%")
operator_menu.grid(row=1, column=1, padx=10, pady=10)

tk.Label(root, text="Second Number:").grid(row=2, column=0, padx=10, pady=10)
entry2 = tk.Entry(root)
entry2.grid(row=2, column=1, padx=10, pady=10)

# Create and place the calculate button
calculate_button = tk.Button(root, text="Calculate", command=calculate)
calculate_button.grid(row=3, column=0, columnspan=2, pady=10)

# Create and place the result label
tk.Label(root, text="Result:").grid(row=4, column=0, padx=10, pady=10)
result_var = tk.StringVar()
result_label = tk.Label(root, textvariable=result_var)
result_label.grid(row=4, column=1, padx=10, pady=10)

# Start the main event loop
root.mainloop()
