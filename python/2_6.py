lst=input("list of name").split()
count=0
for names in lst:
	count+=names.count('a')
	#for char in set(names):
		#if(char=="a"):
			#count+=1
print(count)
