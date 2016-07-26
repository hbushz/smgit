#! /usr/bin/perl -w

undef $/;
$text = <>;
$text =~ s/^$/<p>/mg;
print "$text";
