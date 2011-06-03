#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Problem 20
#
#n! means n × (n − 1) × ... × 3 × 2 × 1
#
#For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
#and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.
#
#Find the sum of the digits in the number 100!

import math

n = 100

tsum = 0

tot = math.factorial(n)

numstr = str(tot)

for i in numstr:
    tsum += int(i)

print tsum
