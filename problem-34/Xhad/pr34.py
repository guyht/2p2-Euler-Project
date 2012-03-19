#!/usr/bin/env python
from __future__ import print_function, division
#I code in Python 3 but am trying to make it backward-compatible

from math import factorial
import time
start = time.clock()

def sumfact(n):
    result = 0
    while n > 0:
        result += factorial(n%10)
        n //= 10
    return result
    
N = 10**7
#7*factorial(9) < 9999999

answer = 0

for i in range(10, N):
    if i == sumfact(i):
        answer += i
        
end = time.clock()-start
        
print('Answer', answer, 'Time:', end*1000, 'ms')