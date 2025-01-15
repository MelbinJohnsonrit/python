import cmath

a=float(input("enter coefficient of a"))
b=float(input("enter coefficient of b"))
c=float(input("enter coefficient of c"))

d=b**2 - 4*a*c

if(d==0):
	print(-b/(2*a))
elif(d>0):
	print((-b+cmath.sqrt(d))/(2*a))
	print((-b-cmath.sqrt(d))/(2*a))
else:
	print((-b+cmath.sqrt(d))/(2*a))
	print((-b-cmath.sqrt(d))/(2*a))

