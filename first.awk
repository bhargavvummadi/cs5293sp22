#!/bin/awk -f 
BEGIN {
	print "HELLO WORLD";
	
	for(i=1;i<10;i++)
	{
		print "The square of ", i, "is",i*i;
	}
}

