import tkinter as tk
from tkinter import messagebox

class FibonacciApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Cognifyz Fibonacci Sequence Generator")

        self.label = tk.Label(root, text="Enter the number of terms:")
        self.label.pack(pady=10)

        self.entry = tk.Entry(root)
        self.entry.pack(pady=10)

        self.generate_button = tk.Button(root, text="Generate", command=self.generate_fibonacci)
        self.generate_button.pack(pady=10)

        self.result_label = tk.Label(root, text="")
        self.result_label.pack(pady=10)

    def generate_fibonacci(self):
        try:
            n = int(self.entry.get())
            if n <= 0:
                raise ValueError("Number of terms must be a positive integer.")

            fibonacci_sequence = self.calculate_fibonacci(n)
            self.result_label.config(text=f"Fibonacci sequence ({n} terms): {fibonacci_sequence}")
        except ValueError as e:
            messagebox.showerror("Invalid Input", str(e))

    def calculate_fibonacci(self, n):
        sequence = []
        a, b = 0, 1
        for _ in range(n):
            sequence.append(a)
            a, b = b, a + b
        return sequence

if __name__ == "__main__":
    root = tk.Tk()
    app = FibonacciApp(root)
    root.mainloop()
