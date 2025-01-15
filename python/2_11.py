lst=input("words").split()
longest=""
for i in lst:
	if(len(i)>len(longest)):
		longest=i
print(longest)
