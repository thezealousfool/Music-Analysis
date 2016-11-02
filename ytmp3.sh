#!/bin/bash

quality=$(youtube-dl -F $1 | grep audio | tail -1 | awk '{print $1;}')

filename=$(youtube-dl --quiet -f "$quality" "$1" --get-filename)
echo "Downloading ${filename%.*}"
youtube-dl --quiet -f "$quality" "$1" 
nfilename="${filename%.*}".mp3
ffmpeg -loglevel panic -i "$filename" "$nfilename"
rm "$filename"
echo "Successfully Downloaded $nfilename"
