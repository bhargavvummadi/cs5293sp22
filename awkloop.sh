#!/bin/awk -f
BEGIN {print "START"	}
{print "From bash file" $1 $2 }
END {print "STOP"}
