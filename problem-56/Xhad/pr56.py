#!/usr/bin/env python
from __future__ import print_function, division
#I code in Python 3 but am trying to make it backward-compatible

import time
start = time.clock()

def sumdigits(n):
    result = 0
    while n > 0:
        result += n % 10
        n //= 10
    return result

answer = 0

A = 100
B = 100

for a in range(A+1):
    for b in range(B+1):
        new = sumdigits(a**b)
        answer = max(new, answer)
        
end = time.clock()-start

print('Answer:', answer, 'Time:', end*1000, 'ms')
