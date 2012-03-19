#!/usr/bin/env python
from __future__ import print_function, division
#I code in Python 3 but am trying to make it backward-compatible

import time
start = time.clock()

N = 1000000

def collatz(n):
    if n % 2 == 0:
        return n//2
    else:
        return 3*n+1

def lencollatz(n, cache={}):
    if n == 1:
        return 1
    if n not in cache:
        cache[n] = 1+lencollatz(collatz(n))
    return cache[n]
    
best = (0,0)
    
for i in range(1, N+1):
    best = max(best, (lencollatz(i), i))
    
answer = best[1]
    
end = time.clock()-start

print('Answer:', answer, 'Time:', end*1000, 'ms')