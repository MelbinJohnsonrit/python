num = int(input("Enter the number of terms: "))
if num <= 0:
	print("Please enter a positive integer.")
else:
	fib_series = []
	a, b = 0, 1
	while len(fib_series) < num:
		fib_series.append(a)
		a, b = b, a + b
	print(fib_series)
