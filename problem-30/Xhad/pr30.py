#!/usr/bin/env python
from __future__ import print_function, division
#I code in Python 3 but am trying to make it backward-compatible

import time
start = time.clock()

#Upper bound determined experimentally by comparing i*9**5 to 10**i-1
CEILING = 10**6
K = 5

def sumK(x):
    result = 0
    tempx = x
    while tempx > 0:
        result += (tempx % 10)**K
        tempx //= 10
    return result

answer = 0

for i in range(10, CEILING+1):
    if i == sumK(i):
        answer += i

end = time.clock()-start

print('Answer:', answer, 'Time:', end*1000, 'ms')