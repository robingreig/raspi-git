#!/bin/bash

if [ -s ./CurrentOfficeTemp ]
then
  echo "CurrentOfficeTemp has data"
  scp -q /home/robin/CurrentOfficeTemp robin@raspi15.hopto.org:/home/robin/CurrentOfficeTemp
else
  echo "CurrentOfficeTemp is empty"
fi
