#! /bin/bash

# i=1
# until [ "$i" -gt 20 ]
# do
#     echo "$i"
#     let "i+=2"
#     if [ "$i" -ge 10 ];then
#         break
#     fi
# done
# echo "Finally we find the value of i is $i."

j=1
while [ "$j" -lt 20 ]
do
    echo "$j"
    let "j+=2"
    if [ "$j" -ge 10 ];then
        break
    fi
done
echo "Finally we find the value of j is $j."
