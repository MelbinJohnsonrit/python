str1 = input("Enter string 1: ")
str2 = input("Enter string 2: ")
s3 = str1[:1]+str2[1]+str1[2:]+" "+str2[:1]+str1[1]+str2[2:]
print(s3)
