#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Problem 7

#By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
#
#What is the 10001st prime number?

VERBOSE = 1

MAX = 10000000
n = 6
sieve = {}
primes = [2]

for i in range(3,MAX):
    if i%2 == 0:
        pass
    else:
        if i not in sieve:
            primes.append(i)
            j = i
            while j < MAX:
                sieve[j] = True # setdefault?
                j +=i

    if len(primes) == 10001:
        break

#print primes
print primes[-1] 
