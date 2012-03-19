#!/usr/bin/env python
from __future__ import print_function, division
#I code in Python 3 but am trying to make it backward-compatible

import time
start = time.clock()



N = 1001

answer = 1
k = 1
for i in range(1, N//2+1):
    for j in range(4):
        k += 2*i
        answer += k

end = time.clock()-start

print('Answer:', answer, 'Time:', end*1000, 'ms')