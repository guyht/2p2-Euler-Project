#!/usr/bin/env python
from __future__ import print_function, division
#I code in Python 3 but am trying to make it backward-compatible

#Brute force.  I think I know a way to prevent some duplication but haven't bothered
#to try implementing it yet.

from itertools import permutations
import time
start = time.clock()

startdigits = '123456789'
resultset = set({})

for p in permutations(startdigits):
    digits = ''.join(p)
    for i in range(1, len(digits)-2):
        for j in range(i+1, len(digits)-1):
            if int(digits[0:i]) * int(digits[i:j]) == int(digits[j:]):
                resultset.add(int(digits[j:]))
                
answer = sum(resultset)
end = time.clock()-start

print('Answer:', answer, 'Time:', end*1000, 'ms')
