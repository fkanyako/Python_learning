# Intro to Tkinter
import tkinter as tk
# from tkinter import ttk

# Create a function


def doorbell(event):
    print("Please ring the doorbell")

window = tk.Tk()

window.geometry("300x200")

alabel = tk.Label(text="This is fun")
alabel.grid(column=0, row=0)

# Creating a visual bottom
blabel = tk.Label(text="Cool")
blabel.grid(column=1, row=0)

button = tk.Button(window, text="doorbell")
button.grid(column=0)  # If you ass column  = o still the same result

button2 = tk.Button(window, text="False")
button2.grid(column=1, row=1)

# Adding event handlers
window.bind("<Button-1>", doorbell)

window.mainloop()