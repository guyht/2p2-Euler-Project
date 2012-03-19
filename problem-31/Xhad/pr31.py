#!/usr/bin/env python
from __future__ import print_function, division
#I code in Python 3 but am trying to make it backward-compatible


#Brute force + memoization

import time
start = time.clock()

def mcountToN(i, N, denoms, runningtotal=0, cache={}):
    if i >= len(denoms):
        return 0
    
    count = 0
    total = runningtotal
    while total < N:
        if (i, total) not in cache:
            cache[(i, total)] = mcountToN(i+1, N, denoms, total)
        count += cache[(i, total)]
        total += denoms[i]
    return (total == N) + count
    

N = 200

denoms = [200, 100, 50, 20, 10, 5, 2, 1]

answer = mcountToN(0, N, denoms)
end = time.clock()-start

print('Answer', answer, 'Time:', end*1000, 'ms')
