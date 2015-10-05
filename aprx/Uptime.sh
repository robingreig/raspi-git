#!/bin/bash

cp ./uptime.txt ./uptime.txt.tmp
date > ./uptime.txt
uptime >> ./uptime.txt
head -4 ./uptime.txt.tmp >> ./uptime.txt

scp ./uptime.txt robin@192.168.200.15:/home/robin/APRX1.uptime.txt

