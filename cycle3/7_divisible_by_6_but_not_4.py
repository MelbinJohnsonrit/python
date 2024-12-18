n=int (input("Enter the limit:"))
sum=0
print("integers that are dibisible by 6 but not 4 :")
for i in range(1,n):
    if (i%6==0)&(i%4!=0):
        sum=sum+i
        print(i)
print("sum of integers that are dibisible by 6 but not 4 :",sum)
