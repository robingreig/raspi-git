#!/bin/sh

cp ./uptime.txt ./uptime.txt.tmp
echo > ./uptime.txt
date >> ./uptime.txt
uptime >> ./uptime.txt
head -6 ./uptime.txt.tmp >> ./uptime.txt
echo >> ./uptime.txt
df -h >> ./uptime.txt
echo >> ./uptime.txt
ifconfig eth0 >> ./uptime.txt

#scp -q /home/robin/uptime.txt robin@raspi15.hopto.org:/home/robin/TemPi120.uptime.txt
scp -P 81 -q /home/robin/uptime.txt robin@raspi15.hopto.org:/home/robin/TemPi120.uptime.txt
