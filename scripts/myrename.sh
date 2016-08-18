#! /bin/bash 

count=1;
for img in `find . -iname '*.jpg' -type f -maxdepth 1`
do
    new=image-$count.${img##*.}
    echo "Renaming $img to $new"
    mv "$img" "$new"
    let count++
done
