#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Problem 15

#Starting in the top left corner of a 2×2 grid, there are 6 routes (without backtracking) to the bottom right corner.
#
#How many routes are there through a 20×20 grid?

# Tried an exhaustive find - took too long.

# For a 1x1 grid the number of paths from all positions is:
# 2--1
# |  |
# 1--end
#
# 2x1
# 3--1
# |  |
# 2--1
# |  |
# 1--end
#
# 3x1
# 4--1
# |  |
# 3--1
# |  |
# 2--1
# |  |
# 1--end
#
# 3x2
# 10--4--1
#  |  |  |
#  6--3--1
#  |  |  |
#  3--2--1
#  |  |  |
#  1--1--end
#
# Number of paths at (x,y) is = (x+1,y) + (x,y+1)
# All the edges only have 1 path.

VERBOSE = False

rows = 20

m=[]

#Create empty matrix
for i in range(rows + 1):
    m.append([])
    for j in range(rows + 1):
        m[i].append(0)

# Fill in edges with 1
for i in range(rows + 1):
    m[rows][i]=1
    m[i][rows]=1
 
if VERBOSE:
    for l in m: print l

#Build matrix
for x in range(rows - 1, -1, -1):
    for y in range(rows - 1, -1, -1):
        m[x][y] = m[x+1][y] + m[x][y+1]

if VERBOSE:
    for l in m:
        print l

print "Solution: %s" % m[0][0]
