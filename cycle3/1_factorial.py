num = int(input("Enter a number: "))
if num < 0:
	print("Sorry, factorial does not exist for negative numbers.")
else:
	result = 1
	for i in range(1, num + 1):
		result *= i
	print(result)

	
