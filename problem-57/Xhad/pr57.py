#!/usr/bin/env python
from __future__ import print_function, division
#I code in Python 3 but am trying to make it backward-compatible

from fractions import Fraction
import time

start = time.clock()

#Brute force + memoization

def contfrac(k, seq, cache={}):
    t = next(seq)
    if k == 1:
        return t
    else:
        #this caching method only works if seq[i] == seq[j] implies seq[i+1] == seq[j+1]
        if (t, k) not in cache:
            cache[(t,k)] = t + Fraction(1, contfrac(k-1, seq))
        return cache[(t,k)]

def twoseq():
    yield 1
    while True:
        yield 2

def numdigits(n):
    return len(str(n))

N = 1000
answer = 0

for i in range(1, 1+N):
    x = contfrac(i, twoseq())
    answer += (numdigits(x.numerator) > numdigits(x.denominator))
    
end = time.clock()-start

print('Answer:', answer, 'Time:', end*1000, 'ms')
