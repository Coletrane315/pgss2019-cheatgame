def ncr(n, r):
    return factorial(n)/(factorial(r)*factorial(n-r))

def factorial(n):
	return 1 if (n<1) else n*factorial(n-1)
