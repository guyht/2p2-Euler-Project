#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Problem 9

#A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
#a^2 + b^2 = c^2

#For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

#There exists exactly one Pythagorean triplet for which a + b + c = 1000.
#Find the product abc.



VERBOSE = 1

def pythag(x, y, h):
    h2 = h*h
    if (x*x + y*y) == h2:
        return True

MAX = 1000

a = 0
b = 1
c = 2

found = False

solution = []

while a < MAX and not found:
    a +=1
    b = a + 1
    while b < MAX and not found:
        c = 1000 - a - b
        found = pythag(a,b,c)
        if found: solution = [a,b,c]
        b += 1

print "Solution: a = %s b = %s c = %s" % (solution[0], solution[1], solution[2])

print "Product: %s" %(solution[0] * solution[1] * solution[2])
