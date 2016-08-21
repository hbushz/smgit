#! /bin/bash

while read line; 
do 
    echo "$line"; 
done <<< "`find . -name "*.txt"`"
# while read line; 
# do 
#     echo "$line"; 
# done < ./log.txt

