#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Problem 1
#
# If we list all the natural numbers below 10 that are multiples of 3 or 5, we 
# get 3, 5, 6 and 9. The sum of these multiples is 23.

# Find the sum of all the multiples of 3 or 5 below 1000.

i = 3

MAX = 1000

max_count = MAX - 1

trees = set()
fives = set()

while i <= max_count:
    if i%3 == 0:
        trees.add(i)
    if i%5 == 0:
        fives.add(i)
    i += 1

both = trees | fives

print sum(both)
