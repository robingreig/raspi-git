#!/bin/sh

# 2014.12.28 Had to change the date to - rather than colon's to be able to copy to the FAT32 usb stick
#mysqldump -u robin -pMicr0s0ft house_stats | gzip > /home/robin/house_stats_backup/house-stats-backup.`date +%F.%H:%M`.sql.gz
mysqldump -u robin -pMicr0s0ft house_stats | gzip > /home/robin/house_stats_backup/house-stats-backup.`date +%F-%H-%M`.sql.gz

#mysqldump -u robin -pMicr0s0ft mediadb | gzip > /home/robin/mediadb_backup/mediadb_backup.`date +%F.%H:%M`.sql.gz


scp -q /home/robin/house_stats_backup/`ls -tp /home/robin/house_stats_backup/ | grep -v /$ | head -1` robin@192.168.200.14:/home/robin/house_stats_backup
scp -q /home/robin/house_stats_backup/`ls -tp /home/robin/house_stats_backup/ | grep -v /$ | head -1` /media/usb/house_stats_backup
scp -q /home/robin/house_stats_backup/`ls -tp /home/robin/house_stats_backup/ | grep -v /$ | head -1` robin@192.168.200.16:/home/robin/house_stats_backup

#scp -q /home/robin/mediadb_backup/`ls -tp /home/robin/mediadb_backup/ | grep -v /$ | head -1` robin@192.168.200.14:/home/robin/mediadb_backup
#scp -q /home/robin/mediadb_backup/`ls -tp /home/robin/mediadb_backup/ | grep -v /$ | head -1` robin@192.168.200.16:/home/robin/mediadb_backup

#scp -q /home/robin/raspi15_backup/`ls -tp /home/robin/raspi15_backup/ | grep -v /$ | head -1` robin@192.168.200.14:/home/robin/raspi15_backup/
#scp -q /home/robin/raspi15_backup/`ls -tp /home/robin/raspi15_backup/ | grep -v /$ | head -1` robin@192.168.200.16:/home/robin/raspi15_backup/

scp -q /home/robin/OfficeTempBackup/`ls -tp /home/robin/OfficeTempBackup/ | grep -v /$ | head -1` robin@192.168.200.14:/home/robin/OfficeTempBackup/
scp -q /home/robin/OfficeTempBackup/`ls -tp /home/robin/OfficeTempBackup/ | grep -v /$ | head -1` /media/usb/OfficeTempBackup/
scp -q /home/robin/OfficeTempBackup/`ls -tp /home/robin/OfficeTempBackup/ | grep -v /$ | head -1` robin@192.168.200.16:/home/robin/OfficeTempBackup/

#scp -q /home/robin/raspi15_backup/raspi15-var-www.`date +%F.%H:%M`.tar.gz robin@192.168.200.14:/home/robin/raspi15_backup



