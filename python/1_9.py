y=int(input("enter year"))
if(y%400==0 or y%4==0 and y%100!=0):
	print("leap")
else:
	print("not")
