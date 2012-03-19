#!/usr/bin/env python
from __future__ import print_function, division
#I code in Python 3 but am trying to make it backward-compatible

import time
start = time.clock()

#The original problem didn't have the input in a file but I found it easier
#Than manually typing all the data into a list
infile = open('pr18input.txt')

pyramid = []

for line in infile:
    row = line.split(' ')
    row = [int(x) for x in row]
    pyramid.append(row)

for i, row in enumerate(pyramid):
    for j, space in enumerate(row):
        left = 0 if i == 0 or j == 0 else pyramid[i-1][j-1]
        right = 0 if i == 0 or j == len(row)-1 else pyramid[i-1][j]

        row[j] += max(left, right)

answer = max(pyramid[-1])

end = time.clock()-start

print('Answer:', answer, 'Time:', end*1000, 'ms')