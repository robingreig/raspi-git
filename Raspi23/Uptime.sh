#!/bin/sh

cp ./uptime.txt ./uptime.txt.tmp
echo > ./uptime.txt
date >> ./uptime.txt
uptime >> ./uptime.txt
head -6 ./uptime.txt.tmp >> ./uptime.txt

#scp /home/robin/uptime.txt robin@raspi15.hopto.org:/home/robin/Raspi23.uptime.txt
scp /home/robin/uptime.txt robin@raspi15.local:/home/robin/Raspi23.uptime.txt

