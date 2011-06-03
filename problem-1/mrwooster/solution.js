#!/usr/bin/env node

var i=0,
    len=1000,
    nums = 0;

for(i=0;i<len;i++) {
    if((i%3 === 0) || (i%5 === 0)) {
        nums += i;
    }
}

console.log(nums);
