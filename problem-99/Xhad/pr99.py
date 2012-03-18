#!/usr/bin/env python
from __future__ import print_function, division
#I code in Python 3 but am trying to make it backward-compatible

from math import log
import time
start = time.clock()

infile = open('../base_exp.txt')

maxn = 0
maxi = -1

for i, line in enumerate(infile, 1):
    base, exponent = (int(x) for x in line.rstrip().split(','))
    n = exponent * log(base)
    if n > maxn:
        maxn = n
        maxi = i
        
end = time.clock() - start
print('Answer:', maxi, 'Time:', end*1000, 'ms')
