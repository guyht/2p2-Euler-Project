#!/usr/bin/env python
from __future__ import print_function, division
#I code in Python 3 but am trying to make it backward-compatible

import time
start = time.clock()

def numberAsWord(n):
    result = ''
    numbers = {1: 'one',
                    2: 'two',
                    3: 'three',
                    4: 'four',
                    5: 'five',
                    6: 'six',
                    7: 'seven',
                    8: 'eight',
                    9: 'nine',
                    10: 'ten',
                    11: 'eleven',
                    12: 'twelve',
                    13: 'thirteen',
                    14: 'fourteen',
                    15: 'fifteen',
                    16: 'sixteen',
                    17: 'seventeen',
                    18: 'eighteen',
                    19: 'nineteen',
                    20: 'twenty',
                    30: 'thirty',
                    40: 'forty',
                    50: 'fifty',
                    60: 'sixty',
                    70: 'seventy',
                    80: 'eighty',
                    90: 'ninety',
                   0: ''
                    }
    
    if n == 1000:
        result = 'onethousand'
    elif n > 100 and n % 100 != 0:
        hundreds = n // 100 % 10
        result += numbers[hundreds] + 'hundredand'
    elif n >= 100:
        hundreds = n // 100 % 10
        result += numbers[hundreds] + 'hundred'
    rest = n % 100
    if rest in numbers:
        result += numbers[rest]
    else:
        if rest >= 10:
            result += numbers[rest//10*10]
        result += numbers[rest % 10]
            
    return result

N = 1000
answer = 0

for i in range(1, N+1):
    answer += len(numberAsWord(i))
        
end = time.clock()-start

print('Answer:', answer, 'Time:', end*1000, 'ms')