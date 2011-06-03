#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Problem 5
# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
#
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

VERBOSE = 1

sol = 0
max_divisor = 20
found = False

while found == False:
    sol += max_divisor
    for i in range(max_divisor,1,-1):
        if sol % i != 0:
            break
        if i == 2:
            found = True

print sol

