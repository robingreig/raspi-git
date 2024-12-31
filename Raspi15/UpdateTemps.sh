#!/bin/bash

/home/robin/raspi-git/Raspi15/UpdateAtticTemp.py
cat /home/robin/CurrentAtticTemp
echo " > CurrentAtticTemp: "

/home/robin/raspi-git/Raspi15/UpdateCeilingTemp.py
cat /home/robin/CurrentCeilingTemp
echo " > CurrentCeilingTemp: "
/home/robin/raspi-git/Raspi15/UpdateDeskTemp.py
cat /home/robin/CurrentGarageTemp
echo " > CurrentDeskTemp: "
/home/robin/raspi-git/Raspi15/UpdateOutsideTemp.py
cat /home/robin/CurrentOutsideTemp
echo " > CurrentOutsideTemp: "
/home/robin/raspi-git/Raspi15/allTempPub01.py


