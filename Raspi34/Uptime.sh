#!/bin/sh

cp ./uptime.txt ./uptime.txt.tmp
echo > ./uptime.txt
date >> ./uptime.txt
uptime >> ./uptime.txt
head -4 ./uptime.txt.tmp >> ./uptime.txt
echo >> ./uptime.txt
ifconfig wlan0>> ./uptime.txt
echo >> ./uptime.txt
df -h >> ./uptime.txt

scp /home/robin/uptime.txt robin@raspi15.local:/home/robin/Raspi34.uptime.txt

