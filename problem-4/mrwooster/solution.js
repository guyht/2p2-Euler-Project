#!/usr/bin/env node

/*
 * A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91  99.
 *
 * Find the largest palindrome made from the product of two 3-digit numbers.
 */

/*
 * The idea is to find all palindromes, add them to an array and find the highest one
 */

var start = new Date().getTime();

function findPalindrome() {
	var a,b, palindrome = [];

	for(a=999;a>99;a--) {
		for(b=999;b>99;b--) {
			if(isPlindrome(a*b)) {
				// Add it to the array
				palindrome[palindrome.length] = a*b;
			}
		}
	}

	// Return the highest palindrome
	palindrome.sort(function(a,b) { return b-a; });
	return palindrome[0];
}


function isPlindrome(num) {
	// Convert to string
	num+='';

	if(num === num.reverse()) {
		return true;
	}

	return false;
}

// Create reverse function for strings
String.prototype.reverse=function(){return this.split("").reverse().join("");};

var ans = findPalindrome();

var stop = new Date().getTime() - start;

console.log('Solution: ' + ans);
console.log('Time Taken: ' + stop + 'ms');
