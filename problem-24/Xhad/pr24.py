#!/usr/bin/env python
from __future__ import print_function, division
#I code in Python 3 but am trying to make it backward-compatible

import time
start = time.clock()

from itertools import permutations

N = 1000000

perm = permutations('0123456789')

for i in range(N-1):
    next(perm)
    
answer = next(perm)

answer = ''.join(c for c in answer)
end = time.clock()-start

print('Answer:', answer, 'Time:', end*1000, 'ms')