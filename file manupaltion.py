import tkinter as tk
from tkinter import filedialog, messagebox
from collections import Counter
import re

class FileManipulationApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Cognifyz File Manipulation - Word Counter")

        self.label = tk.Label(root, text="Select a text file to count word occurrences:")
        self.label.pack(pady=10)

        self.select_button = tk.Button(root, text="Select File", command=self.select_file)
        self.select_button.pack(pady=10)

        self.result_text = tk.Text(root, wrap='word', height=20, width=60)
        self.result_text.pack(pady=10)

    def select_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
        if file_path:
            self.count_words(file_path)

    def count_words(self, file_path):
        try:
            with open(file_path, 'r') as file:
                text = file.read().lower()
                words = re.findall(r'\b\w+\b', text)
                word_counts = Counter(words)
                sorted_word_counts = dict(sorted(word_counts.items()))

                self.result_text.delete(1.0, tk.END)
                self.result_text.insert(tk.END, "Word Count Results:\n")
                for word, count in sorted_word_counts.items():
                    self.result_text.insert(tk.END, f"{word}: {count}\n")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")

if __name__ == "__main__":
    root = tk.Tk()
    app = FileManipulationApp(root)
    root.mainloop()
