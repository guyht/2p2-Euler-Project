#!/usr/bin/env node

// Start time
var time = new Date().getMilliseconds();

var i=0,
    len=1000,
    nums = 0;

for(i=0;i<len;i++) {
    if((i%3 === 0) || (i%5 === 0)) {
        nums += i;
    }
}


var end = new Date().getMilliseconds() - time;

console.log('Solution: ' + nums);
console.log('Time taken: ' + end);
