#!/bin/bash

cp ./uptime.txt ./uptime.txt.tmp
echo > ./uptime.txt
date >> ./uptime.txt
uptime >> ./uptime.txt
head -4 ./uptime.txt.tmp >> ./uptime.txt
echo >> ./uptime.txt
df -h >> ./uptime.txt

scp ./uptime.txt raspi15.local:/home/robin/AdafruitAio1.uptime.txt

