#from datetime import datetime

#today=datetime.today()
#today=datetime.now()
#today=datetime.year()
#print(today)
dob=input('enter your date of birth in the format:YYYY-MM-DD:')
dob_parts=dob.split('-')

year_born=int(dob_parts[0])
month_born=int(dob_parts[1])
day_born=int(dob_parts[2])

today_date=int(input('Enter current date in format:YYYY-MM-DD:'))
today_date_parts=today_date.split("-")
current_year=today_date_parts[0]
current_month=today_date_parts[1]
current_day=today_date_parts[2]

year=current_year - year_born
month_born=current_month-month_born
days=current_day-day_born

if days<0:
    months-=1



