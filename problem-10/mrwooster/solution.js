#!/usr/bin/env node

/*
 * The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
 *
 * Find the sum of all the primes below two million.
 */

var start = new Date();

var floor = 2000000,
	sum=2,i;

function prime(n) {

	var lim = Math.floor(Math.sqrt(n)+1),
		k=2;

	while(k<lim) {
		if(n%k === 0) return false;
		k++;
	}

	return true;
}

for(i=3;i<=floor;i=i+2) {
	if(prime(i)) {
		sum += i;
	}
}

console.log('Time taken ' + (new Date().getTime() - start));

console.log('Sum of primes below 2,000,000 : ' + sum);
