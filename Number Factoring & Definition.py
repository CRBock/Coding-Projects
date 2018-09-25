# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

numfact = input("Number to analyze ")
numfact = int(numfact)
factorlist = []
#divisorlist = range(1,numfact)

for i in range(1,numfact): 
    #while numfact - i > 0:
        if numfact % i == 0:
            factorlist.append(i)
            
factorsum = sum(factorlist)
if factorsum == 1:
        print("Prime")
elif factorsum < numfact:
        print("Deficient")
elif factorsum == numfact:
        print("Perfect")
elif factorsum > numfact:
        print("Abundant")
