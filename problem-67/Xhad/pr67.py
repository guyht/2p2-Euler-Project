#!/usr/bin/env python
from __future__ import print_function, division
#I code in Python 3 but am trying to make it backward-compatible

#Standard dynamic programming solution; go row-by-row and calculate
#"maximal path so far", then extend to the next row

import time
start = time.clock()

infile = open('../triangle.txt')

pyramid = []

for line in infile:
    row = line.split(' ')
    row = [int(x) for x in row]
    pyramid.append(row)

for i, row in enumerate(pyramid):
    for j in range(len(row)):
        #TODO: Read from bottom-up and eliminate the need for these ternaries
        left = 0 if i == 0 or j == 0 else pyramid[i-1][j-1]
        right = 0 if i == 0 or j == len(row)-1 else pyramid[i-1][j]

        row[j] += max(left, right)
        

answer = max(pyramid[-1])
end = time.clock()-start

print('Answer:', answer, 'Time', end*1000, 'ms')
