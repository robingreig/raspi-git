#!/bin/sh
#===========================================
# Filename: BackupOfficeTemp.sh for TemPi17
# Author: Robin Greig
# Date: 2017.05.03
#===========================================

mysqldump -u robin -pMicr0s0ft office_temp | gzip > /home/robin/OfficeTempBackup/office_temp-backup.`date +%F.%H-%M`.tempi110.sql.gz
scp -q /home/robin/OfficeTempBackup/office_temp-backup.`date +%F.%H-%M`.tempi110.sql.gz robin@raspi15.hopto.org:/home/robin/OfficeTempBackup/
#scp -q /home/robin/OfficeTempBackup/office_temp-backup.`date +%F.%H-%M`.tempi110.sql.gz robin@192.168.137.95:/home/robin/OfficeTempBackup/
