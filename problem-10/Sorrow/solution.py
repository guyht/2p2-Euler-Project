#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Problem 10

#The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
#
# Find the sum of all the primes below two million.


VERBOSE = 1

MAX = 2000000
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

print sum(primes)
