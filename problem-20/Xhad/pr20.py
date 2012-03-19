#!/usr/bin/env python
from __future__ import print_function, division
#I code in Python 3 but am trying to make it backward-compatible

import time
start = time.clock()

from math import factorial

N = 100

prod = factorial(N)
answer = 0

while prod > 0:
    answer += prod % 10
    prod //= 10
    
end = time.clock()-start

print('Answer:', answer, 'Time:', end*1000, 'ms')