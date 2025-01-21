import tkinter as tk
from tkinter import ttk

def celsius_to_fahrenheit():
    try:
        celsius = float(entry_celsius.get())
        fahrenheit = (celsius * 9/5) + 32
        entry_fahrenheit.delete(0, tk.END)
        entry_fahrenheit.insert(0, str(fahrenheit))
    except ValueError:
        entry_fahrenheit.delete(0, tk.END)
        entry_fahrenheit.insert(0, "Invalid input")

def fahrenheit_to_celsius():
    try:
        fahrenheit = float(entry_fahrenheit.get())
        celsius = (fahrenheit - 32) * 5/9
        entry_celsius.delete(0, tk.END)
        entry_celsius.insert(0, str(celsius))
    except ValueError:
        entry_celsius.delete(0, tk.END)
        entry_celsius.insert(0, "Invalid input")

# Create the main window
root = tk.Tk()
root.title("Temperature Converter")

# Create and place the widgets
label_celsius = ttk.Label(root, text="Celsius:")
label_celsius.grid(column=0, row=0, padx=10, pady=10)

entry_celsius = ttk.Entry(root)
entry_celsius.grid(column=1, row=0, padx=10, pady=10)

label_fahrenheit = ttk.Label(root, text="Fahrenheit:")
label_fahrenheit.grid(column=0, row=1, padx=10, pady=10)

entry_fahrenheit = ttk.Entry(root)
entry_fahrenheit.grid(column=1, row=1, padx=10, pady=10)

button_c_to_f = ttk.Button(root, text="Convert Celsius to Fahrenheit", command=celsius_to_fahrenheit)
button_c_to_f.grid(column=0, row=2, padx=10, pady=10)

button_f_to_c = ttk.Button(root, text="Convert Fahrenheit to Celsius", command=fahrenheit_to_celsius)
button_f_to_c.grid(column=1, row=2, padx=10, pady=10)

# Run the application
root.mainloop()