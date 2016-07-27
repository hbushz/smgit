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

for dir in $(ls /home)
do
    echo "$dir"
done

# for ((i=1;i<=5;i++))
# do
#     echo "$i"
# done

# for ((i=1;i<=9;i++))
# do
#     for ((j=1;j<=i;j++))
#     do 
#         if [ "$((j % 2))" -eq 1 ]; then
#             continue 
#         fi
#         let product=i*j
#         printf "$i*$j=$product "
#         if [ "$j" -gt 7 ]; then
#             break 
#         fi
#     done
#     printf "\n"
# done
