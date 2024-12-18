nums = [int(num) for num in input("enter list of numbers to find multiple of 3(seperated by space):").split()]

multiples_of_three = list(filter(lambda x: x % 3 == 0, nums))

print("Multiples of 3:", multiples_of_three)
