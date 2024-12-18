import math
ul=9999
ll=1000
l=[]
for i in range(ll,ul):
        even=True
        for digit in str(i):
                if int(digit)%2!=0:
                        even=False
                        break
        if even and math.trunc(math.sqrt(i))**2==i:
                l.append(i)
print(l)

