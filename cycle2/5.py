str = input("Enter a string: ")

if str.endswith("ing"):
    print(str[:-3]+"ly")
else:
    print(str+"ing")
