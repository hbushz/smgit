#! /bin/bash 

# output the line begin with Character T
# result=`awk '/^T/ { print }' scores.txt`

# echo "$result"
result=`awk '/^(T|K)/ && $2>80 { print }' scores.txt`

echo "$result"
