#!/bin/bash

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

scp /home/robin/PicsTemp/* robin@192.168.200.24:/home/robin/Pictures/

#scp /home/robin/PicsTemp/* robin@192.168.200.150:/home/robin/Pictures/

mv /home/robin/PicsTemp/* /home/robin/Pictures/


