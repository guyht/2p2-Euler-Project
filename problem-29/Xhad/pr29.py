#!/usr/bin/env python
from __future__ import print_function, division
#I code in Python 3 but am trying to make it backward-compatible

import time
start = time.clock()

A = 100
B = 100

sequence = set({})

for a in range(2, A+1):
    for b in range(2, B+1):
        sequence.add(a**b)
        
answer = len(sequence)

end = time.clock()-start

print('Answer:', answer, 'Time:', end*1000, 'ms')