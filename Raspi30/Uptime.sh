#!/bin/sh

cp ./uptime.txt ./uptime.txt.tmp
echo > ./uptime.txt
date >> ./uptime.txt
uptime >> ./uptime.txt
head -6 ./uptime.txt.tmp >> ./uptime.txt
echo >> ./uptime.txt
ifconfig wlan0>> ./uptime.txt
echo >> ./uptime.txt
df -h >> ./uptime.txt

scp /home/robin/uptime.txt robin@raspi15.hopto.org:/home/robin/Pi30.uptime.txt

