#!/usr/bin/env node

/*
 * By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
 *
 * What is the 10001st prime number?
 *
 */

var start = new Date().getTime();

var prime = 11; // Good place to start :)
var count = 5;

while(count < 10001) {
	prime++;
	if(isPrime(prime)) count++;
}

function isPrime(num) {
	var x;

	if(num%2 === 0) return false;

	for(x=3;x<=Math.sqrt(num);x+=2) {
		if(num%x === 0) return false;
	}

	return true;
}

end = new Date().getTime() - start;

console.log('Solution: ' + prime);
console.log('Time Taken: ' + end + 'ms');

