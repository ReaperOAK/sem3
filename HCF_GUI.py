import tkinter as tk
from tkinter import ttk

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def calculate_hcf():
    try:
        num1 = int(entry_num1.get())
        num2 = int(entry_num2.get())
        result = gcd(num1, num2)
        label_result.config(text=f"HCF (GCD) is: {result}")
    except ValueError:
        label_result.config(text="Invalid input. Please enter integers.")

# Create the main window
root = tk.Tk()
root.title("HCF (GCD) Calculator")

# Create and place the widgets
label_num1 = ttk.Label(root, text="Enter first number:")
label_num1.grid(column=0, row=0, padx=10, pady=10)

entry_num1 = ttk.Entry(root)
entry_num1.grid(column=1, row=0, padx=10, pady=10)

label_num2 = ttk.Label(root, text="Enter second number:")
label_num2.grid(column=0, row=1, padx=10, pady=10)

entry_num2 = ttk.Entry(root)
entry_num2.grid(column=1, row=1, padx=10, pady=10)

button_calculate = ttk.Button(root, text="Calculate HCF (GCD)", command=calculate_hcf)
button_calculate.grid(column=0, row=2, columnspan=2, padx=10, pady=10)

label_result = ttk.Label(root, text="HCF (GCD) is:")
label_result.grid(column=0, row=3, columnspan=2, padx=10, pady=10)

# Run the application
root.mainloop()