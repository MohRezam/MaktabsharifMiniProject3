#!/bin/bash
file="Icons.txt"
out_dir="/home/digitcrom/Desktop/Miniproject/MaktabsharifMiniProject3/front/Icons"
mkdir $out_dir

while IFS= read -r line; do
    cp "$line" "$out_dir"
done < "$file"

echo "successfully transferred"
