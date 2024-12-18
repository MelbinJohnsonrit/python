def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

def permutations(n, r):
    return factorial(n) // factorial(n - r)

def combinations(n, r):
    return factorial(n) // (factorial(r) * factorial(n - r))

n = int(input("enter n : "))
r = int(input("enter r : "))
print("Permutations (",n,",",r,"):",permutations(n, r))
print("Combinations (",n,",",r,"):",combinations(n, r))
