import cmath

print("Quadratic equation solver : ax^2 + bx + c = 0")
a=float(input("Enter coefficiant of x^2 (a):"))
b=float(input("Enter coefficiant of x (b):"))
c=float(input("Enter constant value (c):"))

d=(b**2)-(4*a*c)
if(d==0):
	sol1=(-b/2*a)
	print("solution 1: ",sol1)
elif(d>0):
	sol1=(-b-math.sqrt(d))/(2*a)
	sol2=(-b+math.sqrt(d))/(2*a)
	print("solution 1: ",sol1)
	print("solution 2: ",sol2)
else: 
	sol1=(-b-cmath.sqrt(d))/(2*a)
	sol2=(-b+cmath.sqrt(d))/(2*a)
	print("solution 1: ",sol1)
	print("solution 2: ",sol2)
