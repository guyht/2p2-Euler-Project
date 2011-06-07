#!/usr/bin/env python

fib1 = 1
fib2 = 2

total = 0

while fib2 < 4000000:
	fib3 = fib1 + fib2
	fib1 = fib2
	fib2 = fib3

	if (fib3%2 == 0):
		total = total + fib3

print str(total+2)
