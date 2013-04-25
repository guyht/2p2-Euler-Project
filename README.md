## 2p2 Project Euler Challenge

Welcome to the 2p2 Project Euler Challenge!

### Step 1
* Fork the GitHub repository

### Step 2
* Use the following directory structure: problem-x -> 2p2username -> solution.ext
* Some problems require common data files (e.g. problem 22).  If this is the case, the first person to solve the problem should add it to the main problem directory for others to use.

### Step 3
* Grinding

### Step 4
* Issue a pull request when you have completed the problem

###Rules
* Solutions should declare their environment and have the correct extension.  E.g. for a python solution, the first line should contain something like `#!/usr/bin/env python`.  This allows other users to execute your solutions.

* Solutions should output the solution (obviously)

* Solutions should profile themselves and output their execution time.  This is helpful in comparing solutions.  The rules for this are that you must profile all code that is executed, with the exception of console logging.  You should output the time taken in milliseconds to the console: `Time Taken: 12345ms`.

Example for a python solution:

    start = time.time()
    # Run your code here
    end = time.time() - start
    print "Time Taken: " + str(end) + "ms"

