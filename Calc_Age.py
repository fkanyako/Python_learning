import datetime

# Year, month, date
dob = datetime.date(1995, 7, 5)
now = datetime.date.today()

his_age = now - dob
# print(now.year)
print(his_age)