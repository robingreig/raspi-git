#!/bin/sh

cp ./uptime.txt ./uptime.txt.tmp
echo > ./uptime.txt
date >> ./uptime.txt
uptime >> ./uptime.txt
head -4 ./uptime.txt.tmp >> ./uptime.txt
echo >> ./uptime.txt
df -h >> ./uptime.txt
echo >> ./uptime.txt
ifconfig eth0 >> uptime.txt

scp /home/robin/uptime.txt robin@raspi15.local:~/Raspi24.uptime.txt
