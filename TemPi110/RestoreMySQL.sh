#!/bin/sh

#mysqldump -u robin -pMicr0s0ft office_temp | gzip > /home/robin/OfficeTempBackup/office_temp-backup.`date +%F.%H-%M`.tempi110.sql.gz
scp robin@192.168.137.85:/home/robin/OfficeTempBackup/`ls -tp robin@192.168.137.85:/home/robin/OfficeTempBackup/ | grep -v /$ | head -1` /home/robin/OfficeTempBackup/.
#scp /home/robin/OfficeTempBackup/ robin@192.168.137.85:/home/robin/OfficeTempBackup/`ls -tp /home/robin/OfficeTempBackup/ | grep -v /$ | head -1`
