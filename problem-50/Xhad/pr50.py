#!/usr/bin/env python
from __future__ import print_function, division
#I code in Python 3 but am trying to make it backward-compatible

from math import sqrt
import time

start = time.clock()

def sieve(n):
    result = list(range(2,n))
    i = 0
    while result[i]**2 < result[-1]:
        result = [x for x in result if x <= result[i] or x % result[i] != 0]
        i += 1
    return result

def longestsum(primes, ceiling):
    k = int(sqrt(ceiling))
    while k > 0:
        start = 0
        end = k
        while end <= len(primes):
            result = sum(primes[start:end])
            if result >= ceiling:
                break
            if result in primes:
                return (result, k)
            start += 1
            end += 1
        k -= 1
        
N = 1000000
primes = sieve(N)

answer = longestsum(primes, N)[0]

end = time.clock()-start

print('Answer:', answer, 'Time:', end*1000, 'ms')
