#!/usr/bin/env python

from __future__ import print_function, division

#I code in Python 3 but am trying to make it backward-compatible

#sumdiff is a dictionary such that sumdiff[a+b] = a-b.  When one of the (a+b)'s is proven to be pentagonal,
#we have our answer (since results are only recorded in the first place if a, b, and a-b are all pentagonal)

import time
start = time.clock()

def p(n):
    return n*(3*n-1)//2

def pr44():
    n = 1
    pk = {p(n)}
    sumdiff = {}

    while True:
        n += 1
        new = p(n)
        if new in sumdiff:
            return sumdiff[new]
        for current in pk:
            if new-current in pk:
                sumdiff[new+current] = new-current
        pk.add(new)
		
answer = pr44()

end = time.clock()

print('Answer:', answer, 'Time:', end*1000, 'ms')
