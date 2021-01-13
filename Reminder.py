import time
from datetime import date,datetime,timedelta

print("What shall I remind you about?")
text = str(input())
print("When shall I remind you?")
reminder_year = input("Please enter reminder's year :")
reminder_month = input("Please enter reminder's month (1-12) :")
reminder_day = input("Please enter reminder's day :")
reminder_hour = input("Please enter reminder's hour :")
reminder_minute = input("please enter reminder's minute :")
reminder_date = datetime(int(reminder_year),
                         int(reminder_month),
                         int(reminder_day),
                         int(reminder_hour),
                         int(reminder_minute),
                         0)

time_diff = reminder_date - datetime.now()
time.sleep(time_diff.total_seconds)
print(text)


