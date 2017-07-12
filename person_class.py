# Create a class called person
# create init method
import datetime


class Person:
    def __init__(self, name, birthdate):
        self.name = name
        self.birthdate = birthdate

    def age(self):
        today = datetime.date.today()
        age = today.year - self.birthdate.year
        return age

Lansana = Person("Hassan", datetime.date(1992, 7, 5))
print(Lansana.name)
print(Lansana.birthdate)
print(Lansana.age())

