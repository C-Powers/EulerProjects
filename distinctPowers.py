#distinctPowers.py
import numpy as np
arrNum=[]
for i in range(1,101):
    arrNum=arrNum+[i]

a=np.array([arrNum],dtype='float64')
b=a

combo=[]
for i in range(0, len(a)):
    for j in range(0, len(b)):
        print a[i]**b[j]
        combo = combo + [a[i]**b[j]]

outArr=[]
for i in range(0, len(combo)):
    if combo.count(combo[i]) == 1 :
        outArr = outArr +[combo[i]]
    else:
        combo[i]=0
        print combo[i]

print outArr
print len(outArr)
