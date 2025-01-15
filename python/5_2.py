import datetime

now=datetime.datetime.now()
print("current date and time",now);

print("current year",now.year);

print("month of the year",now.strftime("%B"))

print("week number of year",now.strftime("%U"))

print("week day of week",now.strftime("%A"))

print("day of year",now.strftime("%j"))

print("day of month",now.day)

print("day of week",now.weekday()+1)
