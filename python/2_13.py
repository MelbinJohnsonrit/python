lst=input("enter sting of word").split()
count=dict()

for word in lst:
	if(word in count):
		count[word]+=1
	else:
		count[word]=1
print(count)
