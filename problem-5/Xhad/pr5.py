#!/usr/bin/env python
from __future__ import print_function, division
#I code in Python 3 but trying to make it backward-compatible

#The method: Find the prime factorization of our answer by finding
#The prime factors of all numbers 2-N.  Then multiply them all together.

import time
start = time.clock()

N = 20

def primefactorization(x):
    result = {}
    i = 2
    while x > 1:
        while x % i == 0:
            result[i] = result.get(i, 0) + 1
            x //= i
        i += 1
                
    return result

factors = {}
for i in range(2, N+1):
    pfs = primefactorization(i)
    for k in pfs:
        factors[k] = max(factors.get(k, 0), pfs[k])
        
answer = 1
for k in factors:
    answer *= k**factors[k]

end = time.clock() - start

print('Answer:', answer, 'Time:', end*1000, 'ms')
