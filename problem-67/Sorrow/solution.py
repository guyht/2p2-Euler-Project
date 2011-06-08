#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
import codecs

start = time.time()

# Problem 18

# By starting at the top of the triangle below and moving to adjacent numbers on the row below, the maximum total from top to bottom is 23.
# 
# 3
# 7 4
# 2 4 6
# 8 5 9 3
# 
# That is, 3 + 7 + 4 + 9 = 23.
# 
# Find the maximum total from top to bottom of the triangle below:

VERBOSE = True


m = []
sol = []

with open("../triangle.txt", 'r') as f:
    for line in f:
        m.append([int(x) for x in line.split()])

for i in range(1,101):
    sol.append([0]*i)

for x, xval in enumerate(m):
    for y, yval in enumerate(xval):
        if x == 0 and y == 0:
            sol[x][y] = m[x][y]
        elif y == 0:
            sol[x][y] = m[x][y] + sol[x-1][y]
        elif x == y:
            sol[x][y] = sol[x-1][y-1] + m[x][y]
        else:
            sol[x][y] = max(sol[x-1][y-1],sol[x-1][y]) + m[x][y]
            
        #for l in sol:
        #    print l

print "Solution: %s" % sorted(sol[-1])[-1]

end = time.time() - start
print "Time Taken: " + str(end) + "ms" 
