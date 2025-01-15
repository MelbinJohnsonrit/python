lst1=list(map(int,input("list1").split()))
lst2=list(map(int,input("list2").split()))

if(len(lst1) == len(lst2)):
	print("same length")
else:
	print("not same length")
sum1=sum(lst1)
sum2=sum(lst2)
if(sum1==sum2):
	print("sum is same")
else:
	print("sum is not same")
out=(check in lst1 for check in lst2)
if(out):
	print("samevalues")
else:
	print("not same values")
