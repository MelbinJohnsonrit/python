list1=[int(num) for num in input("enter list 1 numbers(seperated by space):").split()]
list2=[int(num) for num in input("enter list 2 numbers(seperated by space):").split()]


print("1.Whether lists are of the same length.")
if (len(list1)==len(list2)):
	print("	the list are of same length")
else:
	print("	the list are not same length")


print("2.Whether the list sums to the same value.")
sum1=sum(list1)
sum2=sum(list2)
if (sum1==sum2):
	print("	sum of both list are same")
else:
	print("	sum of both list are not same")


print("3.Whether any value occurs in both Lists.")
out = any(check in list1 for check in list2)
if out:
	print("	true")
else:
	print("	false")
