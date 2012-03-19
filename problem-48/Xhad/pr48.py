#!/usr/bin/env python
from __future__ import print_function, division
#I code in Python 3 but am trying to make it backward-compatible

import time
start = time.clock()

N = 1000
K = 10

def sumpow(n):
    return sum((i**i for i in range(1, 1+n)))
    
answer = sumpow(N) % 10**K
end = time.clock()-start

print('Answer:', answer, 'Time:', end*1000, 'ms')
