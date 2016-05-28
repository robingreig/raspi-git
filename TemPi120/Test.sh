#!/bin/bash

echo >> /home/robin/Test.log

date >> /home/robin/Test.log

/home/robin/officetemp.py

if [ -s ./CurrentOfficeTemp ]
then
#  printf "Sending Office Temperature to Raspi15: "
  echo -n "Sending Office Temperature to Raspi15: "
  cat  /home/robin/CurrentOfficeTemp
#  scp -q /home/robin/CurrentOfficeTemp robin@raspi15.hopto.org:/home/robin/CurrentOfficeTemp
else
  echo "CurrentOfficeTemp is empty"
fi
