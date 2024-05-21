import random
import tkinter as tk
from tkinter import messagebox

class GuessingGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Cognifyz Guessing Game")

        self.number_to_guess = random.randint(1, 100)

        self.label = tk.Label(root, text="I have selected a number between 1 and 100. Can you guess it?")
        self.label.pack(pady=10)

        self.entry = tk.Entry(root)
        self.entry.pack(pady=10)

        self.guess_button = tk.Button(root, text="Guess", command=self.check_guess)
        self.guess_button.pack(pady=10)

        self.result_label = tk.Label(root, text="")
        self.result_label.pack(pady=10)

    def check_guess(self):
        try:
            user_guess = int(self.entry.get())

            if user_guess < self.number_to_guess:
                self.result_label.config(text="Too low! Try again.")
            elif user_guess > self.number_to_guess:
                self.result_label.config(text="Too high! Try again.")
            else:
                messagebox.showinfo("Congratulations!", f"You've guessed the correct number: {self.number_to_guess}")
                self.reset_game()
        except ValueError:
            self.result_label.config(text="Please enter a valid integer.")

    def reset_game(self):
        self.number_to_guess = random.randint(1, 100)
        self.entry.delete(0, tk.END)
        self.result_label.config(text="")

if __name__ == "__main__":
    root = tk.Tk()
    game = GuessingGame(root)
    root.mainloop()