#!/usr/bin/env python
from __future__ import print_function, division
#I code in Python 3 but am trying to make it backward-compatible

#This one is so easy I originally just typed it in the interpreter
#Python clearly optimizes it for you because if you try to make this
#not be a one-liner it takes a lot longer

import time
start = time.clock()
answer = (28433*2**7830457+1) % 10**10
end = time.clock()-start
print('Answer:', answer, 'Time:', end*1000, 'ms')