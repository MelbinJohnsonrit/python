def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

def series_sum(n):
    sum = 0
    for i in range(1, n + 1):
        sum += (i ** i) / factorial(i)
    return sum

n = int(input("enter limit:"))
print("Sum of the series up to ",n," terms:",round(series_sum(n),2))
