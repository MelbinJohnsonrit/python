a=int(input("enter the n1"))
b=int(input("enter the n2"))
c=int(input("enter the n3"))
if(a>b & a>c):
	largest=a
elif(b>a & b>c):
	largest=b
else:
	largest=c
print(largest)
