import tkinter as tk
from tkinter import messagebox

def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def convert_temperature():
    try:
        temperature = float(entry_temp.get())
        unit = unit_var.get()
        
        if unit == 'C':
            converted_temp = celsius_to_fahrenheit(temperature)
            result_label.config(text=f"{temperature}°C is equal to {converted_temp:.2f}°F")
        elif unit == 'F':
            converted_temp = fahrenheit_to_celsius(temperature)
            result_label.config(text=f"{temperature}°F is equal to {converted_temp:.2f}°C")
        else:
            result_label.config(text="Invalid unit of measurement.")
    except ValueError:
        messagebox.showerror("Input Error", "Please enter a valid temperature.")

# Create the main window
root = tk.Tk()
root.title("Temperature Conversion")

# Create and place the temperature entry
tk.Label(root, text="Enter the temperature value:").grid(row=0, column=0, padx=10, pady=10)
entry_temp = tk.Entry(root)
entry_temp.grid(row=0, column=1, padx=10, pady=10)

# Create and place the unit selection
tk.Label(root, text="Select the unit of measurement:").grid(row=1, column=0, padx=10, pady=10)
unit_var = tk.StringVar(value='C')
tk.Radiobutton(root, text="Celsius (C)", variable=unit_var, value='C').grid(row=1, column=1, padx=10, pady=5, sticky='w')
tk.Radiobutton(root, text="Fahrenheit (F)", variable=unit_var, value='F').grid(row=2, column=1, padx=10, pady=5, sticky='w')

# Create and place the convert button
convert_button = tk.Button(root, text="Convert", command=convert_temperature)
convert_button.grid(row=3, columnspan=2, pady=10)

# Create and place the result label
result_label = tk.Label(root, text="")
result_label.grid(row=4, columnspan=2, pady=10)

# Start the main loop
root.mainloop()
