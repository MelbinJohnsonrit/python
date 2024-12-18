def compare(s1, s2, n):
    return s1[:n] == s2[:n]

s1 = input("enter string 1: ")
s2 = input("enter string 2: ")
n = int(input("enter a number to compare string elements: "))
print("Comparison result: ",compare(s1, s2, n))
