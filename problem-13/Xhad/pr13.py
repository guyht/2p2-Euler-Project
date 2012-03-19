#!/usr/bin/env python
from __future__ import print_function, division
#I code in Python 3 but am trying to make it backward-compatible

import time
start = time.clock()

#Not originally a file but I found it easier to process this way
infile = open('pr13input.txt')

answer = str(sum(int(line) for line in infile))[:10]

end = time.clock()-start

print('Answer:', answer, 'Time:', end*1000, 'ms')