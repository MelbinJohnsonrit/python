lst=list(map(int,input("enter no.s").split()))
for i in range(len(lst)):
	if(lst[i]>100):
		lst[i]="over"
print(lst)
