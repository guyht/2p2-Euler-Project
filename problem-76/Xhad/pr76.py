#!/usr/bin/env python

from __future__ import print_function, division

#I code in Python 3 but am trying to make it backward-compatible

#Brute force + memoization!  It literally runs through all possible combos and caches
#the results.  The good news is, it only ends up needing to cache about 2500
#calculations so it's not nearly as inefficient as it looks!
#Without the cache it's pretty disgusting.

import time
start = time.clock()

N = 100

def numsums(n, maxk=0, cache={}):
    maxk = maxk if maxk else n-1
    result = 0
    
    for i in reversed(range(1, maxk+1)):
        if n > i:
            if (n-i, i) not in cache:
                cache[(n-i,i)] = numsums(n-i, i)
            #result += numsums(n-i, i)
            result += cache[(n-i,i)]
        if n == i:
            result += 1
            
    return result

answer = numsums(N)
end = time.clock()-start
	
print('Answer:', answer, 'Time:', end*1000, 'ms')
