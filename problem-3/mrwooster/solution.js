#!/usr/bin/env node

/*
 * The prime factors of 13195 are 5, 7, 13 and 29.
 * What is the largest prime factor of the number 600851475143 ?
 */

// Profile start
var start = new Date().getTime();

var target = 600851475143;
var factor = getPrimeFactor(target);

var stop = new Date().getTime() - start;

console.log('Solution: ' + factor);
console.log('Time Taken: ' + stop + 'ms');

function getPrimeFactor(target) {
	var start = 2,
		i=0,n,j;

	for(i=start;i<target/2;i++) {
		// Test for factor
		if(target%i !== 0) continue;

		n = target/i;

		// Test for odd
		if(n%2 === 0) continue;

		if(!isPrime(n)) continue;

		return n;
	}
}




// Test for prime
function isPrime(n) {
	var max = n/2,
		i=0;

	for(i=2;i<max;i++) {
		if(n%i === 0) return false;
	}

	return true;
}

