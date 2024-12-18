lst=input("enter a list of words (seperated by space):").split()
longest = len(lst[0])
temp = lst[0]
for i in lst:
	if(len(i) > longest):
		longest = len(i)
		temp = i
print("The length of the longest word is:", temp," and length is ", longest)
