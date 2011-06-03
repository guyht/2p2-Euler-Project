#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Problem 6

#The sum of the squares of the first ten natural numbers is,
#12 + 22 + ... + 102 = 385
#
#The square of the sum of the first ten natural numbers is,
#(1 + 2 + ... + 10)2 = 552 = 3025
#
#Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.
#
#Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.


VERBOSE = 1

n = 100

nlist = range(1,n+1)

sum_of_squares = 0
n_total = 0

for i in nlist:
    sum_of_squares += i*i
    n_total += i

square_of_sum = n_total * n_total

print "so2 - 2os = %s" % str(square_of_sum - sum_of_squares)

