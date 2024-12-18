import time
import datetime

current_datetime = datetime.datetime.now()
print("Current date and time:", current_datetime)

current_year = current_datetime.year
print("Current Year:", current_year)

current_year = current_datetime.year
print("Current Year:", current_year)

current_year = current_datetime.year
print("Current Year:", current_year)

current_weekday = current_datetime.strftime("%A")
print("Weekday of the week:", current_weekday)

current_day_of_year = current_datetime.timetuple().tm_yday
print("Day of year:", current_day_of_year)

current_day_of_month = current_datetime.day
print("Day of the month:", current_day_of_month)

current_day_of_week = current_datetime.weekday()
print("Day of week (0=Monday, 6=Sunday):", current_day_of_week)

