#! /bin/bash

# Try if then structure
if [ -f /bin/bash ]
then
    echo "/bin/bash is a file"
fi

if : ; then echo "always true"; fi
