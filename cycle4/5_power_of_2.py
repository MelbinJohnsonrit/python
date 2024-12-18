exponents = [int(num) for num in input("enter list of numbers to find power of 2(seperated by space):").split()]
powers_of_2 = list(map(lambda x: 2 ** x, exponents))

print("\nPowers of 2:",powers_of_2)
