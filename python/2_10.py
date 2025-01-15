lst=list(map(int,input("enter no.s").split()))
lst1=[]
for i in range(len(lst)):
	if(lst[i] % 2 != 0):
		lst1.append(lst[i])
print(lst1)
