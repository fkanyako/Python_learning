# Create a class called person
# create init method
import datetime
import tkinter as tk

# Create frame
window = tk.Tk()

# Create geometry frame
window.geometry("350x350")

# Set the title of the frame
window.title("Age Calculator")

# Adding Labels
year_label = tk.Label(text="Year")
year_label.grid(column=0, row=1)

month_label = tk.Label(text="Month")
month_label.grid(column=0, row=2)

day_label = tk.Label(text="Day")
day_label.grid(column=0, row=3)

year_entry = tk.Entry()
year_entry.grid(column=1, row=1)

month_entry = tk.Entry()
month_entry.grid(column=1, row=2)

day_entry = tk.Entry()
day_entry.grid(column=1, row=3)


def calculate_age():
    print(year_entry.get())
    print(month_entry.get())
    print(day_entry.get())
    person = Person("Hassan", datetime.date(int(year_entry.get()),
                                             int(month_entry.get()),
                                             int(day_entry.get())))
    print(person.age())
    text_answer = tk.Text(master=window,height=10, width=30)
    text_answer.grid(column=1, row=5)
    answer_text = "{name} is {age} years old".format(name=person.name, age=person.age())
    text_answer.insert(tk.END, answer_text)

# Adding a button
calc_button = tk.Button(text="Calculate", command=calculate_age)
calc_button.grid(column=1, row=4)


class Person:
    def __init__(self, name, birthdate):
        self.name = name
        self.birthdate = birthdate

    def age(self):
        today = datetime.date.today()
        age = today.year - self.birthdate.year
        return age

person = Person("Hassan", datetime.date(1992, 7, 5))
# print(Lansana.name)
# print(Lansana.birthdate)
# print(Lansana.age())

window.mainloop()

