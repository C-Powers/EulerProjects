import numpy as np

def fibCal(array):
    index=np.argmax(array)
    newNumber=array[index]+array[index-1]
    return newNumber


def fibTack(oldArr, newVal):
    returnArray = oldArr+[newVal]
    return returnArray


def fibFactor(inArr):
    if inArr/2.==int(inArr/2.) and inArr<4000000:
        return inArr
