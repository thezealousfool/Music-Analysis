#!/bin/bash

OIFS="$IFS"
IFS=$'\n'
path="$@"
files=$(find "$path" -type f -name "*.mp3")
# echo "$files"

if [ ! -d "Plots" ]
	then
		mkdir "Plots"
fi

for file in $files
do
	file_name="${file##*/}"
	file_base="${file_name%.*}"
	python "v1.py" "$file" Plots/"$file_base".plot
done
IFS="$OIFS"