#!/usr/bin/env python
from __future__ import print_function, division
#I code in Python 3 but am trying to make it backward-compatible

from math import factorial
import time
start = time.clock()

def factsum(n):
    result = 0
    temp = n
    while temp > 0:
        result += factorial(temp % 10)
        temp //= 10
    return result

N = 1000000
K = 60

maxchains = {}
count = 0

for i in range(1, N):
    currentnum = i
    currentchain = []
    while currentnum not in maxchains and currentnum not in currentchain:
        currentchain.append(currentnum)
        currentnum = factsum(currentnum)

    offset = maxchains.get(currentnum, 0)
    for j, link in enumerate(reversed(currentchain)):
        maxchains[link] = j+1+offset
        if link < N and j+1+offset == K:
            count += 1

end = time.clock()-start
            
print('Answer:', count, 'Time:', end*1000, 'ms')
