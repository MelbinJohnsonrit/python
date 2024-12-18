total=0
lst=[int (num) for num in input("enter list of numbers (seperated by space):").split()]
for i in range (0,len(lst)):
	total= total+lst[i]
print("sum of all items in list",total)

