#! /bin/bash
# testing the for statement

# for num in 1 2 3 4 5
# do
#     echo "The number is $num"
# done

# for num in {1..8}
# do
#     echo "The number is $num"
# done

# for day in Mon Tue Wed Thu Fri Sat Sun
# do
#     echo "$day"
# done

for dir in $(ls /tmp)
do
    echo "$dir"
done

for ((i=1;i<5;i++))
do
    echo "$i"
done
