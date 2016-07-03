#! /bin/bash 

# output the line begin with Character T
result=`awk '/^T/ { print }' scores.txt`

echo "$result"
