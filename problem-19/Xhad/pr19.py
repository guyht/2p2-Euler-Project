#!/usr/bin/env python
from __future__ import print_function, division
#I code in Python 3 but am trying to make it backward-compatible

import time
start = time.clock()

DAYS = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat']

def advance_days(currentday, elapsed):
    return (currentday+elapsed) % len(DAYS)

def is_leap(year):
    if year % 4 != 0:
        return False
    else:
        return (year % 400 == 0) or (year % 100 != 0)

current = 2
answer = 0

for year in range(1901, 2001):
    months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if is_leap(year):
        months[1] = 29

    for month in months:
        current = advance_days(current, month)
        if DAYS[current] == 'Sun':
            answer += 1

end = time.clock()-start

print('Answer:', answer, 'Time:', end*1000, 'ms')
