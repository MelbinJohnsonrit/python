def is_prime(num):
	if num <= 1:
		return False
	for i in range(2, int(num ** 0.5) + 1):
		if num % i == 0:
			return False
	return True
def nth_prime(n):
	count = 0
	num = 2
	while True:
		if is_prime(num):
			count += 1
			if count == n:
				return num
		num += 1
n = int(input("enter postion number:"))
print(f"\nThe {n}th prime number is: {nth_prime(n)}")
