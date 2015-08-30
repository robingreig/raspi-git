#!/bin/sh

cp ./uptime.txt ./uptime.txt.tmp
date > ./uptime.txt
uptime >> ./uptime.txt
head -4 ./uptime.txt.tmp >> ./uptime.txt

scp -q /home/robin/uptime.txt robin@raspi15.hopto.org:/home/robin/Raspi103.uptime.txt
