#!/bin/sh

cp ./uptime.txt ./uptime.txt.tmp
echo > ./uptime.txt
date >> ./uptime.txt
uptime >> ./uptime.txt
head -4 ./uptime.txt.tmp >> ./uptime.txt
echo >> ./uptime.txt
df -h >> ./uptime.txt
echo >> ./uptime.txt
ifconfig eth0 >> ./uptime.txt

#scp -P 81 -q /home/robin/uptime.txt robin@robin.webhop.me:/home/robin/Raspi15.uptime.txt
scp /home/robin/uptime.txt robin@raspi34.local:/home/robin/Raspi15.uptime.txt
