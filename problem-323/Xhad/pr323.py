#!/usr/bin/env python
from __future__ import print_function, division
#This is actually Python 3 code but I'm trying to make it backward compatible

#Since the state of every bit is independent of the others,
#this is a pretty direct estimate of EV(max of 32 geometric random variables)
#Just proceed from the (infinite series) definition and stop when the terms
#are smaller than the requested precision

import time
start = time.clock()

N = 32
tol = 1e-11

def F(k):
    return (1-(.5)**k)**N

def p(k):
    return F(k) - F(k-1)

evsum = 0
k = 1
ek = 1

while ek > tol:
    ek = k*p(k)
    evsum += ek
    k += 1

end = time.clock()-start

print('Answer: {0:.10f}'.format(evsum), 'Time:', end*1000, 'ms')
