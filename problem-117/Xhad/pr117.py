#!/usr/bin/env python
from __future__ import print_function, division
#I code in Python 3 but am trying to make it backward-compatible

#Inspired by my problem 76 solution, and barely different really.

import time
start = time.clock()

N = 50
seq = [i for i in range(2, 5)]
seq.reverse()

def numsums(n, seq, cache={}):
    result = 0

    if n == 1 or n == 0:
        return 1
    
    for i in seq:
        if n > i:
            if (n-i) not in cache:
                cache[(n-i)] = numsums(n-i, seq)
            result += cache[(n-i)]
        if n == i:
            result += 1

    if (n-1) not in cache:
        cache[(n-1)] = numsums(n-1, seq)

    result += cache[(n-1)]
            
    return result

answer = numsums(N, seq)
end = time.clock()-start

print('Answer:', answer, 'Time:', end*1000, 'ms')
