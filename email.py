import tkinter as tk
from tkinter import messagebox
import re

def is_valid_email(email):
    # Define a regular expression for validating an email address
    email_regex = re.compile(
        r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"
    )
    
    # Match the email string with the regular expression
    if email_regex.match(email):
        return True
    else:
        return False

def validate_email():
    email = entry_email.get()
    if is_valid_email(email):
        result_label.config(text=f"'{email}' is a valid email address.", fg="green")
    else:
        result_label.config(text=f"'{email}' is not a valid email address.", fg="red")

# Create the main window
root = tk.Tk()
root.title("Email Validator")

# Create and place the email entry
tk.Label(root, text="Enter the email address:").grid(row=0, column=0, padx=10, pady=10)
entry_email = tk.Entry(root)
entry_email.grid(row=0, column=1, padx=10, pady=10)

# Create and place the validate button
validate_button = tk.Button(root, text="Validate", command=validate_email)
validate_button.grid(row=1, columnspan=2, pady=10)

# Create and place the result label
result_label = tk.Label(root, text="")
result_label.grid(row=2, columnspan=2, pady=10)

# Start the main loop
root.mainloop()
