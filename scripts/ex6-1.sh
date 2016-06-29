#! /bin/bash

function CountLength()
{
    str=$1
    result=0
    if [ -n "$str" ];then
        # counting the number of characts in the string
        result=${#str}
    fi
    echo "This script name is $0"
    echo "$result"
}
len=$(CountLength "name")
echo "The length is $len"
echo $0
