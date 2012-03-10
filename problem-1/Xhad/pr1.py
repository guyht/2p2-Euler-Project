#!/usr/bin/env python
from __future__ import print_function, division
#This is actually Python 3 code but I'm trying to make it backward compatible

import time
start = time.clock()

threes = {i for i in range(1000) if i % 3 == 0}
fives = {i for i in range(1000) if i % 5 == 0}

end = time.clock()-start

print(sum(threes | fives), end*1000, 'ms')
