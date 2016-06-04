#!/bin/bash

head -12 /home/robin/CurrentOfficeTemp.log > /home/robin/CurrentOfficeTemp.log.tmp

echo > /home/robin/CurrentOfficeTemp.log

date

/home/robin/officetemp.py

if [ -s ./CurrentOfficeTemp ]
then
  echo -n "CurrentOfficeTemp has data & sending to Raspi15: "
  cat /home/robin/CurrentOfficeTemp
  #scp -q /home/robin/CurrentOfficeTemp robin@raspi15.hopto.org:/home/robin/CurrentOfficeTemp
  scp -P81 -q /home/robin/CurrentOfficeTemp robin@raspi15.hopto.org:/home/robin/CurrentOfficeTemp
else
  echo "CurrentOfficeTemp is empty"
fi

cat /home/robin/CurrentOfficeTemp.log.tmp >> /home/robin/CurrentOfficeTemp.log

