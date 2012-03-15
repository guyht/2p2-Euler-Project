#!/usr/bin/env python

from __future__ import print_function, division

#I code in Python 3 but am trying to make it backward-compatible

#Inspired by my problem 76 solution, and barely different really.

import time
start = time.clock()

def numsums(n, seq, cache):
    result = 0

    if n == 1 or n == 0:
        return 1
    
    for i in seq:
        if n > i:
            if (n-i-1) not in cache:
                cache[(n-i-1)] = numsums(n-i-1, seq, cache)
            result += cache[(n-i-1)]
        if n == i:
            result += 1

    if (n-1) not in cache:
        cache[(n-1)] = numsums(n-1, seq, cache)
    result += cache[(n-1)]
            
    return result

k = 1
M = 50
CEILING = 10**6

while True:
    seq = [i for i in range(M, k+1)]
    current = numsums(k, seq, {})
    if current > CEILING:
        break
    k += 1

end = time.clock()-start

print('Answer:', k, 'Time:', end*1000, 'ms')