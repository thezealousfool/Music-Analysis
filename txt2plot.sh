#!/bin/bash

OIFS="$IFS"
IFS=$'\n'
path="$@"
files=$(find "$path" -type f -name "*.plot.txt")
# echo "$files"

if [ ! -d "Plots" ]
	then
		mkdir "Plots"
fi

for file in $files
do
	file_name="${file##*/}"
	file_base="${file_name%.*}"
	mv $file $path/$file_base
done
IFS="$OIFS"