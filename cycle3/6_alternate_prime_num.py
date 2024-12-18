#n = int(input("Enter the limit"))

def is_prime(num):
	if num<2:
		return False
	for i in range (2,int(num**0.5)+1):
		if num % i ==0:
			return False
	return True

n = int(input("Enter the limit"))
print("alternative primes")
p_count=0
num=2
while (num<=n):
	if is_prime(num):
		if p_count%2==0:
			print(num)
		p_count+=1
	num+=1
