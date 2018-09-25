# -*- coding: utf-8 -*-
"""
Created on Wed Sep 19 17:03:25 2018

@author: Admin
"""

ranstart = input("Range start: ")
ranstart = int(ranstart)
ranend = input("Range end: ")
ranend = int(ranend)
factorlist = []
primelist = []
abundantlist = []
perfectlist = []
deficientlist = []
#divisorlist = range(1,numfact)

for i in range(ranstart, ranend,1): 
    factorlist = []
    for x in range(1, ranend): 
        if i % x == 0:
            factorlist.append(x)
    factorsum = sum(factorlist)
    if factorsum == 1:
        primelist.append(i)
    elif factorsum < i:
        deficientlist.append(i)
    elif factorsum == i:
        perfectlist.append(i)
    elif factorsum > i:
        abundantlist.append(i)
