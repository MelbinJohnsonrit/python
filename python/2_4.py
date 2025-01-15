s=input("string")

for char in set(s):
	counts=s.count(char)
	print(char,":",counts)
