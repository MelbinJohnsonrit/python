age=int(input("Enter the age:"))
if(age>0):
	if(age<10):
		print("ticket rate is 7")
	#elif(age>10) or (age<60):
	#	print("ticket rate is 10")
	elif(age>60):
		print("ticket rate is 5")
	elif(age>10) or (age>60):
                print("ticket rate is 10")

else:
	print("Enter a valid age:")


