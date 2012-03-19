#!/usr/bin/env python
from __future__ import print_function, division
#I code in Python 3 but am trying to make it backward-compatible

import time
start = time.clock()

#Explanation of bounds:
#r must be a 1-digit number because 10**k always has k+1 digits
#k was experimentally determined by comparing 9**k to numdigits(k)
#9**22 has 21 digits so combined with the requirement that r is 1-digit,
#we know k-values above 21 are impossible

def numdigits(n):
    return len(str(n))

count = 0

for k in range(1, 22):
    for r in range(1,10):
        if numdigits(r**k) == k:
            count += 1
            
end = time.clock()-start

print('Answer:', count, 'Time:', end*1000, 'ms')
