#!/usr/bin/env python
from __future__ import print_function, division
#I code in Python 3 but am trying to make it backward-compatible

import time
start = time.clock()

N = 1000000

def ispalindrome(n):
    temp = n[::-1]
    return n.lstrip('0') == temp

answer = 0
for i in range(1, N+1):
    if ispalindrome(str(i)) and ispalindrome(bin(i)[2:]):
        answer += i
        
end = time.clock()-start

print('Answer:', answer, 'Time:', end*1000, 'ms')
