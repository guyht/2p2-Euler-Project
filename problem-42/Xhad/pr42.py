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

def cipher(c):
    if c.isalpha():
        return ord(c.upper())-ord('A')+1
    else:
        return 0

infile = open('../words.txt')
triangles = Triangles()

answer = 0

for line in infile:
    for word in line.split(','):
        current = sum(cipher(c) for c in word)
        answer += (current in triangles)
        
end = time.clock()-start

print('Answer:', answer, 'Time:', end*1000, 'ms')
