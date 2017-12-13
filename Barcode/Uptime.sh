#!/bin/sh

cp ./uptime.txt ./uptime.txt.tmp
echo > ./uptime.txt
date >> ./uptime.txt
uptime >> ./uptime.txt
head -4 ./uptime.txt.tmp >> ./uptime.txt
echo >> ./uptime.txt
ifconfig eth0 >> ./uptime.txt
echo >> ./uptime.txt
df -h >> ./uptime.txt

scp -P81 -q /home/robin/uptime.txt robin@raspi15.hopto.org:/home/robin/Raspi21.uptime.txt
