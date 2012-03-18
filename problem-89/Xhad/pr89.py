#!/usr/bin/env python
from __future__ import print_function, division
#I code in Python 3 but am trying to make it backward-compatible

import time
start = time.clock()

#It turns out that this problem is a lot easier if we treat combinations
#as separate tokens instead of looking at individual letters and trying to
#work out their surroundings...

NUMTABLE = (('M', 1000),
            ('CM', 900),
            ('D', 500),
            ('CD', 400),
            ('C', 100),
            ('XC', 90),
            ('L', 50),
            ('XL', 40),
            ('X', 10),
            ('IX', 9),
            ('V', 5),
            ('IV', 4),
            ('I', 1))

def arabictoroman(n):
    result = ''
    temp = n
    for r, a in NUMTABLE:
        while temp >= a:
            result += r
            temp -= a
    return result

def romantoarabic(n):
    result = 0
    temp = n[:]
    while temp:
        for r, a in NUMTABLE:
            if temp.startswith(r):
                result += a
                temp = temp[len(r):]
                break
    return result

infile = open('../roman.txt')

saved = 0

for line in infile:
    current = str(line)
    current = current.strip()
    num = romantoarabic(current)
    improved = arabictoroman(num)
    saved += len(current)-len(improved)
    
end = time.clock()-start

print('Answer:', saved, 'Time:', end*1000, 'ms')
