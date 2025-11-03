#from datetime import datetime

#today=datetime.today()
#today=datetime.now()
#today=datetime.year()
#print(today)
dob = input("Enter your date of birth in the format YYYY-MM-DD: ")
dob_parts = dob.split('-')

year_born = int(dob_parts[0])
month_born = int(dob_parts[1])
day_born = int(dob_parts[2])

today_date = input("Enter current date in format YYYY-MM-DD: ")
today_date_parts = today_date.split('-')

current_year = int(today_date_parts[0])
current_month = int(today_date_parts[1])
current_day = int(today_date_parts[2])

year = current_year - year_born
months = current_month - month_born
days = current_day - day_born

# Adjust days if negative
if days < 0:
    months -= 1
    if current_month == 1:
        prev_month = 12
    else:
        prev_month = current_month - 1

    # Handle number of days in the previous month
    if prev_month in [1, 3, 5, 7, 8, 10, 12]:
        days += 31
    elif prev_month in [4, 6, 9, 11]:
        days += 30
    else:
        days += 28

# Adjust months if negative
if months < 0:
    months += 12
    year -= 1

print(f"Your age is: {year} years, {months} months, and {days} days.")
