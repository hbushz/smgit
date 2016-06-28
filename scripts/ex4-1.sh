#! /bin/bash

# Program:
#    User input a filename, program will check the following:
#    1. exist
#    2. file/directory
#    3. file permissions

echo -e "Please inpute a filename, I will check the filename's type and permission. \n\n"
read -p "Input filename: "  -t 30 filename
test -z $filename && echo "You MUST input a filename." && exit 0
test ! -e $filename && echo "The filename $filename Do Not exist" && exit 0

test -f $filename && filetype="regulare filename"
test -d $filename && filetype="directory"
test -r $filename && permission="readable"
test -w $filename && permission="writable"
test -x $filename && permission="excutable"

echo "The filename: $filename is a $filetype"
echo "And the permission are: $permission"
