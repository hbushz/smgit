#! /bin/bash

read -p "Please enter a score: " -t 30 score

if [ -z "$score" ]
then
    echo "You enter nothing. "
    read -p "Please enter a score: " -t 30 score
fi

if [ "$score" -lt 0 -o "$score" -gt 100 ]
then
    echo "The score must be between 0 and 100. Please enter again: "
    read -p "Please enter again : " -t 30 score
fi

if [ "$score" -ge 60 ]; then
    echo "Congratulations, you pass the exam!"
else
    echo "Come on, let's try again."
fi
