import numpy as np
from math import sqrt

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



arrIt=np.arange(3, 15, 2)

primes=[]
for i in range(1, len(arrIt)):
    maybePrime=is_prime(i)
    if (maybePrime ==True):
        primes = primes + [i]
        print primes
        print np.argmax(primes)
    if (np.argmax(primes)==1):
        print "yep"#primes[np.argmax(primes)]

#print primes
#print np.argmax(primes)
#print primes[10000]
