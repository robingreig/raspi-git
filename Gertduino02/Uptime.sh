#!/bin/bash

cp ./uptime.txt ./uptime.txt.tmp
echo > ./uptime.txt
date >> ./uptime.txt
uptime >> ./uptime.txt
head -6 ./uptime.txt.tmp >> ./uptime.txt

#scp ./uptime.txt raspi15.hopto.org:/home/robin/Gertduino2.uptime.txt
scp ./uptime.txt raspi15.local:/home/robin/Gertduino2.uptime.txt

