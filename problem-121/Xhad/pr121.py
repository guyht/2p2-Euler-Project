#!/usr/bin/env python
from __future__ import print_function, division
#I code in Python 3 but am trying to make it backward-compatible

#Pretty much brute force.  An obvious optimization would be to make the function
#stop making recursive calls whenever the game is definitively decided one
#way or the other.

from math import floor
import time
start = time.clock()

def play_game(n, turns, score=0):
    if turns == 1:
        if score > (n-1)/2:
            return 1
        elif score < (n-1)/2-1:
            return 0
        else:
            return 1/n
    
    return (1/n)*play_game(n+1, turns-1, score+1) + (n-1)/n*play_game(n+1, turns-1, score)

def ev(turns):
    return floor(1/play_game(2,turns))

N = 15
answer = ev(N)

end = time.clock()-start

print('Answer:', answer, 'Time:', end*1000, 'ms')
