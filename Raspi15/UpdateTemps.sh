#!/bin/bash

/home/robin/raspi-git/Raspi15/UpdateAtticTemp.py
echo -n "CurrentAtticTemp: "
cat /home/robin/CurrentAtticTemp
echo ""

/home/robin/raspi-git/Raspi15/UpdateCeilingTemp.py
echo -n "CurrentCeilingTemp: "
cat /home/robin/CurrentCeilingTemp
echo ""

/home/robin/raspi-git/Raspi15/UpdateDeskTemp.py
echo -n "CurrentDeskTemp: "
cat /home/robin/CurrentGarageTemp
echo ""

/home/robin/raspi-git/Raspi15/UpdateOutsideTemp.py
echo -n "CurrentOutsideTemp: "
cat /home/robin/CurrentOutsideTemp
echo ""

/home/robin/raspi-git/Raspi15/UpdateBasementTemp.py
echo -n "CurrentBasementTemp: "
cat /home/robin/CurrentBasementTemp
echo ""

/home/robin/raspi-git/Raspi15/allTempPub01.py


