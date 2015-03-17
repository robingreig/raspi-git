#!/bin/sh

mysqldump -u robin -pMicr0s0ft office_temp | gzip > /home/robin/OfficeTempBackup/office_temp-backup.`date +%F.%H-%M`.tempi110.sql.gz
scp -q /home/robin/OfficeTempBackup/office_temp-backup.`date +%F.%H-%M`.tempi110.sql.gz robin@raspi15.hopto.org:/home/robin/OfficeTempBackup/
scp -q /home/robin/OfficeTempBackup/office_temp-backup.`date +%F.%H-%M`.tempi110.sql.gz robin@192.168.137.245:/home/robin/OfficeTempBackup/


