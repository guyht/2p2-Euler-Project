#!/usr/bin/env python
from __future__ import print_function, division
#I code in Python 3 but am trying to make it backward-compatible

import time
start = time.clock()

N = 1000

a, b = 1, 1
answer = 2

while b < 10**(N-1):
    a, b = b, a+b
    answer += 1
    
end = time.clock()-start

print('Answer:', answer, 'Time:', end*1000, 'ms')