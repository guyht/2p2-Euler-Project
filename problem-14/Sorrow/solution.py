#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Problem 14

#The following iterative sequence is defined for the set of positive integers:
#
#n → n/2 (n is even)
#n → 3n + 1 (n is odd)
#
#Using the rule above and starting with 13, we generate the following sequence:
#13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
#
#It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.
#
#Which starting number, under one million, produces the longest chain?
#
#NOTE: Once the chain starts the terms are allowed to go above one million.

# First attempt at playing with a 'generator'

def sequence_generator(n):
    yield n
    while n > 1:
        if n % 2 == 0:
            n = n/2
        else:
            n = 3 * n + 1
        yield n

maxlen = 0

for i in range(2,1000000):
    tmp = [val for val in sequence_generator(i)]
    length = len(tmp)
    if (length > maxlen):
        maxlen = length
        print "i: %s length: %s" %(i, maxlen)

print maxlen
