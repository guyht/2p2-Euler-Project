#!/usr/bin/env python
from __future__ import print_function, division
#I code in Python 3 but am trying to make it backward-compatible

import time

start = time.clock()

def digits(x):
    return sorted(str(x))

i = 1

while not (digits(2*i) == digits(3*i) == digits(4*i) == digits(5*i) == digits(6*i)):
    i += 1
    
end = time.clock()-start

print('Answer:', i, 'Time:', end*1000, 'ms')
