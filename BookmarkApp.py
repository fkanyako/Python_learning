# Intro to Tkinter
import tkinter as tk
import webbrowser
# from tkinter import ttk

# Create a function


def doorbell(event):
    print("Please ring the doorbell")


def open_green_africa(event):
    webbrowser.open_new_tab('http://www.greenafricanow.com/')


def open_facebook(event):
    webbrowser.open_new_tab("https://www.facebook.com/")

window = tk.Tk()

window.geometry("300x200")

alabel = tk.Label(text="Doorbell")
alabel.grid(column=0, row=0, padx=40, pady=5)

# Creating a visual bottom
# Adding the padx=10, pady=10 allow you to add space around the buttons
blabel = tk.Label(text="Website")
blabel.grid(column=1, row=0, padx=40, pady=5)

clabel = tk.Label(text="Facebook")
clabel.grid(column=1, row=4, padx=40, pady=5)

button = tk.Button(window, text="doorbell")
button.grid(column=0, row=1)  # If you ass column  = o still the same result

button2 = tk.Button(window, text="Green Africa")
button2.grid(column=1, row=1)

button3 = tk.Button(window, text="Login")
button3.grid(column=1, row=5)

# Adding event handlers
button.bind("<Button-1>", doorbell)
button2.bind("<Button-1>", open_green_africa)
button3.bind("<Button-1>", open_facebook)

window.mainloop()