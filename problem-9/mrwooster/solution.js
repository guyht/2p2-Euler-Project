#!/usr/bin/env node

/*
 * A Pythagorean triplet is a set of three natural numbers, a  b  c, for which,
 *
 * a2 + b2 = c2
 * For example, 32 + 42 = 9 + 16 = 25 = 52.
 *
 * There exists exactly one Pythagorean triplet for which a + b + c = 1000.
 * Find the product abc.
 */

function triplet(a, b, c) {
	return (((a*a) + (b*b)) === (c*c)) && (a < b) && (b < c) && (a + b + c === 1000);
}

var i,j,k, A = [], B = [], C = [];

// Setup some arrays
for(i=1;i<1000;i++) {
	for(j=1;j<1000;j++) {
		A = i;
		B = j;
		C = 1000 - i - j
		if(triplet(A, B, C)) {
				console.log('Found solution. A: ' + A + ' B: ' + B + ' C: ' + C + ' Product : ' + (A*B*C));
				return;
		}
	}
}

