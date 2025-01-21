import tkinter as tk
from tkinter import ttk

def kmh_to_ms():
    try:
        kmh = float(entry_kmh.get())
        ms = kmh * (1000 / 3600)
        entry_ms.delete(0, tk.END)
        entry_ms.insert(0, str(ms))
    except ValueError:
        entry_ms.delete(0, tk.END)
        entry_ms.insert(0, "Invalid input")

def ms_to_kmh():
    try:
        ms = float(entry_ms.get())
        kmh = ms * (3600 / 1000)
        entry_kmh.delete(0, tk.END)
        entry_kmh.insert(0, str(kmh))
    except ValueError:
        entry_kmh.delete(0, tk.END)
        entry_kmh.insert(0, "Invalid input")

# Create the main window
root = tk.Tk()
root.title("Speed Converter")

# Create and place the widgets
label_kmh = ttk.Label(root, text="Km/hr:")
label_kmh.grid(column=0, row=0, padx=10, pady=10)

entry_kmh = ttk.Entry(root)
entry_kmh.grid(column=1, row=0, padx=10, pady=10)

label_ms = ttk.Label(root, text="m/s:")
label_ms.grid(column=0, row=1, padx=10, pady=10)

entry_ms = ttk.Entry(root)
entry_ms.grid(column=1, row=1, padx=10, pady=10)

button_kmh_to_ms = ttk.Button(root, text="Convert Km/hr to m/s", command=kmh_to_ms)
button_kmh_to_ms.grid(column=0, row=2, padx=10, pady=10)

button_ms_to_kmh = ttk.Button(root, text="Convert m/s to Km/hr", command=ms_to_kmh)
button_ms_to_kmh.grid(column=1, row=2, padx=10, pady=10)

# Run the application
root.mainloop()