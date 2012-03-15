#!/usr/bin/env python

from __future__ import print_function, division

#I code in Python 3 but am trying to make it backward-compatible

#Inspired by my problem 76 solution, and barely different really.
#There is probably a cleaner way to cache results than with the class but this
#Was literally lifted from a bunch of similar problems and I didn't bother to rethink the rest of it

import time
start = time.clock()

N = 50

class Sequence():
    def __init__(self, seq):
        self.seq = seq
        self.cache = {}

rseq = Sequence([2, 1])
gseq = Sequence([3, 1])
bseq = Sequence([4, 1])
seqs = (rseq, gseq, bseq)

def numsums(n, S):
    result = 0
    
    for i in S.seq:
        if n > i:
            if (n-i) not in S.cache:
                S.cache[(n-i)] = numsums(n-i, S)
            result += S.cache[(n-i)]
        if n == i:
            result += 1
            
    return result

def sumsums(N, seqs):
    result = 0
    for seq in seqs:
		#The -1 is to eliminate "all black tiles" as a solution
        result += numsums(N, seq)-1
    return result
	
answer = sumsums(N, seqs)
end = time.clock()-start

print('Answer:', answer, 'Time:', end*1000, 'ms')