#!/usr/bin/env python
# -*- coding: utf-8 -*-

# The prime factors of 13195 are 5, 7, 13 and 29.
#
# What is the largest prime factor of the number 600851475143 ?

VERBOSE = 0

def primefactors(n):
    """Function a list of prime factors of n"""
    seq = []
    val = 2
    while val <= n:
        if VERBOSE: print "val: %s n: %s" % (val, n)
        if n % val == 0:
            # Found a factor, shrink n by that factor 
            # ie. n = 60, val = 2
            # Next pass n = 30, val = 2
            seq.append(val)
            n /= val
        else:
            # Not (or no longer) a factor
            val += 1

    return seq

l = primefactors(600851475143)

print l

