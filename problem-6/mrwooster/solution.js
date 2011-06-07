#!/usr/bin/env node

/*
 * The sum of the squares of the first ten natural numbers is,
 *
 * 12 + 22 + ... + 102 = 385
 * The square of the sum of the first ten natural numbers is,
 *
 * (1 + 2 + ... + 10)2 = 552 = 3025
 * Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025  385 = 2640.
 *
 * Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
 */

var start = new Date().getTime();

var i,
	sumSquare=0,
	squareSum=0;
// Sum of the squares
for(i=1;i<=100;i++) {
	sumSquare += (i*i);
	squareSum += i;
}

// Square the sum
squareSum = squareSum*squareSum;


end = new Date().getTime() - start;

console.log('Solution: ' + ( squareSum - sumSquare));
console.log('Time Taken: ' + end + 'ms');

