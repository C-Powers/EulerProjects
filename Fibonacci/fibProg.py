import numpy as np
import fibFunc

#Create my starting array, saves time dealing with indeces
fibArr=[1,2,3]

#this next part gives me a starting value for newVal, to tack onto my new array
newVal=fibFunc.fibCal(fibArr)

#Go through 40 iterations, tacking on newVal to the original fibArr each time.
for i in range(1, 40):
    fibArr=fibFunc.fibTack(fibArr, newVal)
    newVal=fibFunc.fibCal(fibArr)

#this is my new array.
#Note, that this has values that exceed 4 million.
print fibArr

#This is where we find the values that are divisible by two AND less than 4mil
factorArray=[]
for i in range(0,len(fibArr)):
    factorGet=fibFunc.fibFactor(fibArr[i])
    factorArray= factorArray+[factorGet]

#get rid of "None" in array
finalFactored=[x for x in factorArray if x is not None]

#the answer!!!
print "------- and the answer is!!!! -------"
print finalFactored
print "Final Sum = ", np.sum(finalFactored)
