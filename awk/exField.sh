#! /bin/awk -f 

{
	x=($2+$3+$4+$5)/4
	grade=(x>85?"Good":"ok")
	print $1,FS,grade 
}
