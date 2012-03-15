#!/usr/bin/env python
from __future__ import print_function, division
#This is actually Python 3 code but I'm trying to make it backward compatible

import time
start = time.clock()

N = 4000000

def fibgen(ceiling):
    xnm1, xn = 1, 1
    while xn < ceiling:
        yield xn
        xnm1, xn = xn, xn+xnm1

end = time.clock()-start
        
print('Answer:', sum(i for i in fibgen(N) if i % 2 == 0), 'Time:', end*1000, 'ms')
        
