#!/bin/bash

cp ./uptime.txt ./uptime.txt.tmp
echo > ./uptime.txt
date >> ./uptime.txt
uptime >> ./uptime.txt
head -4 ./uptime.txt.tmp >> ./uptime.txt
echo >> ./uptime.txt
df -h >> ./uptime.txt
echo >> ./uptime.txt
ifconfig eth0 >> ./uptime.txt

scp /home/robin/uptime.txt robin@raspi20.local:/home/robin/Aprx11.uptime.txt
