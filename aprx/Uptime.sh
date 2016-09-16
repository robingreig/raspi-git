#!/bin/bash

cp ./uptime.txt ./uptime.txt.tmp
echo > ./uptime.txt
date > ./uptime.txt
uptime >> ./uptime.txt
head -4 ./uptime.txt.tmp >> ./uptime.txt
echo >> ./uptime.txt
df -h >> ./uptime.txt

scp ./uptime.txt robin@raspi15.local:/home/robin/Aprx2.uptime.txt

