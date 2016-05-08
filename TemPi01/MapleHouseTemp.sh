#!/bin/sh

echo >> ./MapleHouseTemp.txt
date > ./MapleHouseTemp.txt
echo >> ./MapleHouseTemp.txt
uptime >> ./MapleHouseTemp.txt
echo >> ./MapleHouseTemp.txt
ifconfig wlan0 >> ./MapleHouseTemp.txt
echo >> ./MapleHouseTemp.txt
cat ./MapleHouseTemp >> ./MapleHouseTemp.txt
echo >> ./MapleHouseTemp.txt

scp /home/robin/MapleHouseTemp.txt robin@raspi15.hopto.org:/home/robin/MapleHouseTemp.txt

