str = input("Enter a string: ")
st=str[0]
en=str[-1]
swap_str = en + str[1:-1] + st
print(swap_str)
