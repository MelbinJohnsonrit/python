import calendar

n=int(input("enter year"))
if(calendar.isleap(n)):
	print("leap year")
else:
	print("not leap year")
