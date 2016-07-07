import numpy as np
import math

def is_prime(n):
    if n >1:
        if n == 2:
            return true
        if n % 2 ==0:
            return False
        for current in range(3, int(math.sqrt(n)+1), 2):
            if n % current == 0:
                return False
        return True
    return False

def get_primes(n):
    while True:
        if is_prime(n):
            yield n
        n+=1


def solve_number_10():
    total = 2
    for next_prime in get_primes(3):
        if next_prime < 2000000:
            total += next_prime
        else:
            print(total)
            return

solve_number_10()
