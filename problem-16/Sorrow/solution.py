#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Problem 16
#
#2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
#
#What is the sum of the digits of the number 2^1000?

import math

n = 1000

tsum = 0

tot = int(math.pow(2,n))
print tot

numstr = str(tot)

for i in numstr:
    tsum += int(i)

print tsum
