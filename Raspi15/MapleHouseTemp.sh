#!/bin/sh

tail -n1 /home/robin/MapleHouseTemp.txt > /home/robin/CurrentMapleHouseTemp
cp /home/robin/MapleHouseTemp.txt /home/robin/MapleHouseTemp/MapleHouseTemp.`date +%F-%H-%M`.txt



