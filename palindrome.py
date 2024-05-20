import tkinter as tk
from tkinter import messagebox

def is_palindrome(s):
    s = ''.join(char.lower() for char in s if char.isalnum())
    return s == s[::-1]

def check_palindrome():
    string = entry.get()
    if is_palindrome(string):
        messagebox.showinfo("Palindrome Check", f'"{string}" is a palindrome.')
    else:
        messagebox.showinfo("Palindrome Check", f'"{string}" is not a palindrome.')

# Main window setup
root = tk.Tk()
root.title("Palindrome Checker")

# Entry field for user input
entry = tk.Entry(root, width=40)
entry.pack(pady=10)

# Button to check palindrome
check_button = tk.Button(root, text="Check Palindrome", command=check_palindrome)
check_button.pack()

# Start the main loop
root.mainloop()

