import tkinter as tk
from tkinter import messagebox
import re

class PasswordStrengthChecker:
    def __init__(self, root):
        self.root = root
        self.root.title("Cognifyz Password Strength Checker")

        self.label = tk.Label(root, text="Enter your password:")
        self.label.pack(pady=10)

        self.entry = tk.Entry(root, show='*')
        self.entry.pack(pady=10)

        self.check_button = tk.Button(root, text="Check Strength", command=self.check_strength)
        self.check_button.pack(pady=10)

        self.result_label = tk.Label(root, text="")
        self.result_label.pack(pady=10)

    def check_strength(self):
        password = self.entry.get()
        strength_message = self.evaluate_password(password)
        self.result_label.config(text=strength_message)

    def evaluate_password(self, password):
        if len(password) < 8:
            return "Password is too short! Must be at least 8 characters."

        if not re.search(r'[A-Z]', password):
            return "Password must contain at least one uppercase letter."

        if not re.search(r'[a-z]', password):
            return "Password must contain at least one lowercase letter."

        if not re.search(r'[0-9]', password):
            return "Password must contain at least one digit."

        if not re.search(r'[\W_]', password):
            return "Password must contain at least one special character."

        return "Password is strong!"

if __name__ == "__main__":
    root = tk.Tk()
    app = PasswordStrengthChecker(root)
    root.mainloop()
