import random
import tkinter as tk
from tkinter import messagebox

class NumberGuesser:
    def __init__(self, root):
        self.root = root
        self.root.title("Cognifyz Number Guesser")

        self.lower_bound = 1
        self.upper_bound = 100
        self.number_to_guess = random.randint(self.lower_bound, self.upper_bound)

        self.label = tk.Label(root, text=f"Guess the number between {self.lower_bound} and {self.upper_bound}")
        self.label.pack(pady=10)

        self.entry = tk.Entry(root)
        self.entry.pack(pady=10)

        self.guess_button = tk.Button(root, text="Guess", command=self.check_guess)
        self.guess_button.pack(pady=10)

        self.result_label = tk.Label(root, text="")
        self.result_label.pack(pady=10)

        self.reset_button = tk.Button(root, text="Reset", command=self.reset_game)
        self.reset_button.pack(pady=10)

    def check_guess(self):
        try:
            user_guess = int(self.entry.get())

            if user_guess < self.lower_bound or user_guess > self.upper_bound:
                self.result_label.config(text=f"Please enter a number between {self.lower_bound} and {self.upper_bound}.")
            elif user_guess < self.number_to_guess:
                self.result_label.config(text="Too low! Try again.")
            elif user_guess > self.number_to_guess:
                self.result_label.config(text="Too high! Try again.")
            else:
                messagebox.showinfo("Congratulations!", f"You've guessed the correct number: {self.number_to_guess}")
                self.reset_game()
        except ValueError:
            self.result_label.config(text="Please enter a valid integer.")

    def reset_game(self):
        self.number_to_guess = random.randint(self.lower_bound, self.upper_bound)
        self.entry.delete(0, tk.END)
        self.result_label.config(text="")

if __name__ == "__main__":
    root = tk.Tk()
    game = NumberGuesser(root)
    root.mainloop()