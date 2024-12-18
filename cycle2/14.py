print("a)positive list")
nums=list(map(int,input("Enter intergers:").split()))
positive= [ x for x in nums if x>0]
print(positive)

print("b)square of n ")
n= int(input("Enter number:"))
square= [x**2 for x in range (1, n+1)]
print(square)

print("c)display vowels")
word =input ("enter a word:")
vowels=[char for char in word if char in 'aeiouAEIOU']
print(vowels)

print("d)ordinal value")
word=input ("enter a word :")
ord_values= [ord(char)for char in word]
print(ord_values)
