#! /bin/bash

i=1
until [ "$i" -gt 10 ]
do
    echo "$i"
    let "i+=2"
done
echo "Finally we find the value of i is $i."
