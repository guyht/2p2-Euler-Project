#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Problem 17
#
#If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.
#
#If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?
#
#NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.

VERBOSE = 0

words = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
tens = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
decs = ["twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]

one_through_99 = []

all_words = []

for w in words:
    one_through_99.append(w)

for w in tens:
    one_through_99.append(w)

for d in decs:
    one_through_99.append(d)
    for w in words:
        one_through_99.append("%s %s" %(d, w))

for w in one_through_99:
    all_words.append(w)

for w in words:
    all_words.append("%s hundred" % w)
    for d in one_through_99:
        all_words.append("%s hundred and %s" %(w, d))
       
all_words.append("one thousand")

chars = ""

for a in all_words:
    if VERBOSE: print a
    chars += a

print len(chars.replace(' ', ''))
