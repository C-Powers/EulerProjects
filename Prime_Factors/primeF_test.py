import numpy as np
from math import sqrt

#This function tells me if a factor is prime or not.
def factors(n):
    return list(reduce(list.__add__,
                ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))

def mrange(start,stop,step):
    while start < stop:
        yield start
        start += step

def is_prime(num):
    if num == 2:
        return True
    if (num < 2) or (num % 2 == 0):
        return False
    return all(num % i for i in mrange(3, int(sqrt(num)) + 1, 2))


n=factors(600851475143)
print "List of Factors = ", n

#This loops through the factos of a number, tests whether or not a
#factor is prime, and then returns that number is true.
primeNumbs_n=[]
for i in range(0,len(n)):
    nn=is_prime(n[i])
    if nn==True:
        primeNumbs_n=primeNumbs_n+[n[i]]

print "List of Prime Numbers = ", primeNumbs_n
print "Largest Prime = ", np.amax(primeNumbs_n)
