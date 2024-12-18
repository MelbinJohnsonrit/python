bp=float(input("Enter Basic Pay:"))
if bp<0:
    print("Basic pay must be a positive number")
else:
    hra=bp*0.1
    ta=bp*0.05
    ts=bp+hra+ta
    print("Total Salary:",ts)
