import numpy as np


#This function tells me if a factor is prime or not.
def factors(n):
    return list(reduce(list.__add__,
                ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))
# This function tells me if the number is prime or not
def itPrime(inNumber):
    return all(inNumber % i for i in range(2, inNumber))


n=factors(1000)
print "List of Factors = ", n

#This loops through the factos of a number, tests whether or not a
#factor is prime, and then returns that number is true.
primeNumbs_n=[]
for i in range(0,len(n)):
    nn=itPrime(n[i])
    if nn==True:
        primeNumbs_n=primeNumbs_n+[n[i]]

print "List of Prime Numbers = ", primeNumbs_n
print "Largest Prime = ", np.amax(primeNumbs_n)
