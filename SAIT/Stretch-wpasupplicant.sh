#!/bin/sh
# temporary fix for WPA Enterprise on Raspbian Buster, connect Ethernet before running
sudo apt-get remove wpasupplicant -y
sudo mv -f /etc/apt/sources.list /etc/apt/sources.list.bak
sudo bash -c "echo 'deb http://raspbian.raspberrypi.org/raspbian/ stretch main contrib non-free rpi' > /etc/apt/sources.list"
sudo apt-get update -y
sudo apt-get install wpasupplicant -y
sudo apt-mark hold wpasupplicant
sudo mv -f /etc/apt/sources.list.bak /etc/apt/sources.list
sudo apt-get update -y
