#!/bin/sh

mysqldump -u robin -pMicr0s0ft office_temp | gzip > /home/robin/OfficeTempBackup/office_temp-backup.`date +%F.%H-%M`.tempi110.sql.gz
#scp -q /home/robin/OfficeTempBackup/office_temp-backup.`date +%F.%H-%M`.tempi110.sql.gz robin@50.93.51.6:/home/robin/OfficeTempBackup/
scp /home/robin/OfficeTempBackup/`ls -tp /home/robin/OfficeTempBackup/ | grep -v /$ | head -1` robin@raspi15.hopto.org:/home/robin/OfficeTempBackup/
scp /home/robin/OfficeTempBackup/`ls -tp /home/robin/OfficeTempBackup/ | grep -v /$ | head -1` robin@192.168.137.95:/home/robin/OfficeTempBackup/


