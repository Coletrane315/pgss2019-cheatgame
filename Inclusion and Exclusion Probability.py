numberOfHoles = 0

probability = 0

#hand number
h = 1

#calculates factorials
def factorial(n):
    return 1 if (n==1 or n==0) else n * factorial(n-1);

#Combinatorial function
def combination(n,k):
    return factorial(n)/(factorial(k)*factorial(n-k));

print(factorial(4))

print(combination (4,2))
    
        
    
