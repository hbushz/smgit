#!  /usr/bin/perl
#
$text = "The population of 1367700is growing";

$text =~ s/(?<=\d)(?=(\d\d\d)+(?!\d))/,/g;
print "$text";
