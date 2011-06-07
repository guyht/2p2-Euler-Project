#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Problem 25

#The Fibonacci sequence is defined by the recurrence relation:
#
#    Fn = Fn−1 + Fn−2, where F1 = 1 and F2 = 1.
#
#Hence the first 12 terms will be:
#
#    F1 = 1
#    F2 = 1
#    F3 = 2
#    F4 = 3
#    F5 = 5
#    F6 = 8
#    F7 = 13
#    F8 = 21
#    F9 = 34
#    F10 = 55
#    F11 = 89
#    F12 = 144
#
#The 12th term, F12, is the first term to contain three digits.
#
#What is the first term in the Fibonacci sequence to contain 1000 digits?


def fibonacci():
    """Function returns the Fibonacci sequence with max value of n as an ordered list of ints"""
    a,b = 1,1
    while True:
        yield a
        a,b = b,a+b

for i, seq in enumerate(fibonacci(), start=1):
    chars = "%s" % seq
    if len(chars) >= 1000:
        print i
        break
