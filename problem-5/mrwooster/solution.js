#!/usr/bin/env node

/*
 * 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
 *
 * What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
 */

var start = new Date().getTime();

var num = 2520; // We know it is going to be at least this big (see question)

while(!evenlyDivisible(num)) {
	num++;
}

function evenlyDivisible(n) {
	var i=0;

	for(i=2;i<=20;i++) {
		if(n%i !==0) return false;
	}

	return true;
}

end = new Date().getTime() - start;

console.log('Solution: ' + num);
console.log('Time Taken: ' + end + 'ms');

