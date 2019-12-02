#!/bin/bash
input="png.txt"
while IFS= read -r line
do
  echo "$line"
  cp $line ./
done < "$input"
