#! /usr/bin/perl

print "Enter a temperature in temperature (e.g., 32F, 100C): \n";
$input = <STDIN>;
chomp($input);		#delete the \n of the input

if ( $input =~ m/^([+-]?[0-9]+(\.[0-9]*)?)\s*([CF])$/i )
{
	$InputNum = $1;
	$type = $3;

	if ( $type =~ m/c/i )
	{
		$celsius = $InputNum;
		$fahren = ($celsius*9/5)+32;
	}
	else
	{
		$fahren = $InputNum;
		$celsius = ( $fahren - 32 )*5/9;
	}
	printf "%.2f C is %.2f F\n", $celsius, $fahren;
} 
else 
{
	print "Expecting a number followed by \"C\" or \"F\"\n";
	print "so I don't understand \"$input\".\n";
}
