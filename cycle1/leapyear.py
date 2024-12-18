yr=int(input("Enter the year:"))
if(yr>0):
	if (yr%4 == 0 and yr%100 != 0) or yr%400 == 0 :
		print(yr,"is a leap year")
	else:
		print(yr,"is not a leap year")
else:
	print("Enter a valid year")
