#!/bin/sh
# Add SAIT IP addresses for NTP servers
sudo cp -f /etc/systemd/timesyncd.conf /etc/systemd/timesyncd.conf.bak
sudo bash -c "echo 'NTP= 10.197.2.9 10.197.3.9' >> /etc/systemd/timesyncd.conf.bak"

