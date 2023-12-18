#!/bin/bash

# cd to Pictures directory to run file changes
cd /home/robin/Pictures/

# for file in *.png; do mv "$file" "${file/_h.png/_half.png}"; done

# Remove spaces and replace with .
for file in *" "*; do mv "$file" "${file// /.}"; done

# Replace first : with .
for file in ./*:*
do
  mv -- "$file" "${file/:/.}"
done

# Replace second : with .
for x in ./*:*
do
  mv -- "$x" "${x/:/.}"
done

# cd back to home directory once done
cd /home/robin/
