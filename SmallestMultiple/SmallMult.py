import numpy as np

def calculate():
    target=10
    num_to_test=0
    while True:
        num_to_test += target
        if all(num_to_test % j == 0 for j in range(1,target+1)):
            return num_to_test
    return -1


print calculate()
