#! /usr/bin/perl -w

# $price = 1/4;
$price = 9.0500337;
$price =~ s/(\.\d\d[1-9]?)\d*/$1/;

print "The price is $price\n";
