#proj1.py
#Project 1
#Write a code that will find factors below 1000
#That are factorable by 3 and/or 5

import numpy as np

array1000=np.arange(0,1000)


multArr=[]
for i in range(0, len(array1000)):
  if int(array1000[i]/3.)==array1000[i]/3. or int(array1000[i]/5.)==array1000[i]/5.:
    print array1000[i]
    multArr=multArr+[array1000[i]]


#Done
#CPowers, 1.11.16
#print "Array of Multiples = ", multArr
print "Sum of the multiples of 3 or 5 below 1000 = ", np.sum(multArr)
