#!/bin/bash

cp ./uptime.txt ./uptime.txt.tmp
date > ./uptime.txt
uptime >> ./uptime.txt
head -4 ./uptime.txt.tmp >> ./uptime.txt

scp ./uptime.txt raspi15.local:/home/robin/Gertduino2.uptime.txt

