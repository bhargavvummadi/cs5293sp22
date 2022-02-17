BEGIN FS=","  {print "START"};
{sum=0};
{sum+$2};
END {print sum "STOP"}

