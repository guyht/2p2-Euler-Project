#!/usr/bin/env python
from __future__ import print_function, division
#I code in Python 3 but am trying to make it backward-compatible

from fractions import Fraction
from functools import reduce
from operator import mul
import time

#This is ugly.  I'll probably update it when it's not the only one in it's directory.  ;)

start = time.clock()

def product(X):
    return reduce(mul, X)

results = []

for d in range(2, 101):
    for n in range(1, d):
        num = str(n)
        denom = str(d)
        current = Fraction(n, d)
        if n % 10 != 0 or d % 10 != 0:
            for digit in num[:]:
                while digit in num and digit in denom:
                    num = num.strip(digit) if len(num) - len(num.strip(digit)) < 2 else num[0]
                    denom = denom.strip(digit) if len(denom) - len(denom.strip(digit)) < 2 else denom[0]
            if num.strip('0') and denom.strip('0') and (int(num) != n or int(denom) != d) and Fraction(int(num),int(denom)) == current:
                results.append(current)
                
answer = product(results).denominator
end = time.clock()-start

print('Answer:', answer, 'Time:', end*1000, 'ms')