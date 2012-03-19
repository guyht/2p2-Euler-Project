#!/usr/bin/env python
from __future__ import print_function, division
#I code in Python 3 but am trying to make it backward-compatible

import time
start = time.clock()

class Triangles():
    def __init__(self):
        self.cached = {1}
        self.k = 1
        self.maximum = 1

    def __contains__(self, n):
        while self.maximum < n:
            self.gennext()
        return n in self.cached

    def gennext(self):
        self.k += 1
        self.maximum = self.k*(self.k+1)//2
        self.cached.add(self.maximum)

class Pentagonals():
    def __init__(self):
        self.cached = {1}
        self.k = 1
        self.maximum = 1

    def __contains__(self, n):
        while self.maximum < n:
            self.gennext()
        return n in self.cached

    def gennext(self):
        self.k += 1
        self.maximum = self.k*(3*self.k-1)//2
        self.cached.add(self.maximum)

class Hexagonals():
    def __init__(self):
        self.cached = {1}
        self.k = 1
        self.maximum = 1

    def __contains__(self, n):
        while self.maximum < n:
            self.gennext()
        return n in self.cached

    def gennext(self):
        self.k += 1
        self.maximum = self.k*(2*self.k-1)
        self.cached.add(self.maximum)

triangles = Triangles()
pentagonals = Pentagonals()
hexagonals = Hexagonals()

#40755 is given in the problem, so we start by stepping past that
k = 40756
k in triangles, k in pentagonals, k in hexagonals
classes = (triangles, pentagonals, hexagonals)

while True:
    if classes[0].maximum == classes[1].maximum == classes[2].maximum:
        break
    for i in range(len(classes)):
        while classes[i].maximum < classes[i-1].maximum:
            classes[i].gennext()
    
end = time.clock()-start

print('Answer:', classes[0].maximum, 'Time:', end*1000, 'ms')
