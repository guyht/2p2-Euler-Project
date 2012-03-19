#!/usr/bin/env python
from __future__ import print_function, division
#I code in Python 3 but am trying to make it backward-compatible

import time
start = time.clock()

def sumsquares(nums):
    return sum(x**2 for x in nums)

def squaresum(nums):
    return sum(nums)**2

N = 100

answer = abs(sumsquares(range(1, N+1)) - squaresum(range(1, N+1)))
    
end = time.clock()-start

print('Answer:', answer, 'Time:', end*1000, 'ms')