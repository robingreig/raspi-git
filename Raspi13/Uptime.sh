#!/bin/sh

cp ./uptime.txt ./uptime.txt.tmp
echo > ./uptime.txt
date >> ./uptime.txt
uptime >> ./uptime.txt
head -6 ./uptime.txt.tmp >> ./uptime.txt
echo >> ./uptime.txt
df -h >> ./uptime.txt

scp -P81 /home/robin/uptime.txt robin@raspi15.hopto.org:~/Raspi13.uptime.txt
