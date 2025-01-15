from palin import*

def longest_palin(s):

	num_char=len(s)
	longest=""
	for i in range(num_char):
		for j in range(i+1,num_char+1):
			substring=s[i:j]
			if(palin(substring) and len(substring) > len(longest)):
				longest=substring
	return longest

s=input("enter string")
print(longest_palin(s))
