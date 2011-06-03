#include <stdio.h>
#include <stdlib.h>

// Euler project problem 1

main( ) {
	int i;
	int len = 1000;
	int nums = 0;

	for(i=0;i<len;i++) {
		if((i%3 == 0) || (i%5 == 0)) {
			nums = nums + i;
		}
	}

	char buf[5];
	sprintf(buf, "%d", nums);
	printf("%s\n", buf);
	return 0;
}
