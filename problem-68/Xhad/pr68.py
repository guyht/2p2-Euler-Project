#!/usr/bin/env python
from __future__ import print_function, division
#I code in Python 3 but am trying to make it backward-compatible

from itertools import permutations
import time

start = time.clock()

#Deliberately excluding 10; the '16 digit' requirement means 10 is necessarily
#an outer node, and due to rotational symmetry I can arbitrarily put it in any
#branch I like without skipping possibilities
NODES = [i for i in range(1,10)]

#My format for the graph is a list with the inner nodes first followed by the
#outer nodes.  Respectively, they start at the top point of the pentagon and the
#outer node connected to that point, going clockwise in both cases

def ismagic(graph):
    seed = graph[9] + graph[4] + graph[0]
    for i in range(5, 9):
        if (graph[i] + graph[i-5] + graph[i-4]) != seed:
            return False
    else:
        return True

def graphstring(graph):
    triples = [(graph[i], graph[i-5], graph[i-4]) for i in range(5,9)] + [(graph[9], graph[4], graph[0])]
    pivot = triples.index(min(triples))
    triples = triples[pivot:] + triples[:pivot]
    return ''.join(str(triple[i]) for triple in triples for i in range(len(triple)))
    
def magicgraphs():
    for perm in permutations(NODES):
        perm = list(perm)
        perm.append(10)
        if ismagic(perm):
            yield graphstring(perm)

maxstring = max(magicgraphs())
        
end = time.clock() - start

print('Answer:', maxstring, 'Time:', end*1000, 'ms')