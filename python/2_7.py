cl1=input("color list").split()
cl2=input("color list").split()

cl=list(set(cl1)-set(cl2))
print(cl)

