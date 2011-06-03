#!/usr/bin/env python

# Speed test.  Compare two or more solutions.
#
# Each solution must be executable (chmod +x) and must have then environment
# declaration at the top of the file

import sys
import time
import subprocess
import getopt
import re

def usage():
	print "Usage:"
	print ""
	print "speedTest.py -[hn] file1 file2 file3"
	print ""
	print "Options:"
	print "         -n Number of times to test each solution, default 1000"
	print "         -h Display this usage information"
	print ""
	print "Example:"
	print "       speedTest.py -n 500 ./user1/solution.py ./user2/solution.py"


argv = sys.argv[1:]

# Default to 10 runs
_num_runs = 10
FNULL = open("/dev/null", "w")

try:
	opts, args = getopt.getopt(argv, "hn:")
except getopt.GetoptError:
	usage()
	sys.exit()

# Loop through args
for opt, arg in opts:
	if opt == "-h":
		usage()
		sys.exit()
	elif opt == "-n":
		_num_runs = int(arg)

print "Running " + str(_num_runs) + " times for each solution"

# Check at least one file
if len(args) == 0:
	usage()
	sys.exit()

# Now run tests
for solution in args:
	times = []

	print "Testing solution " + solution

	for x in range(1,_num_runs):
		start = time.time()
		subprocess.call(solution, stdout=FNULL)
		times.append(time.time() - start)

	average = sum(times)/_num_runs
	print "Average execution time: " + str(average)



