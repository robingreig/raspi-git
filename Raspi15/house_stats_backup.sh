#!/bin/sh

# Test with local file save
#newdate=`date -I`
#mysqldump -u root -pMicr0s0ft house_stats | gzip > /home/robin/house_stats-backup.$newdate.sql.gz

# Use ssh to transfer backup file to raspi11

# mysqldump to mediadb backup on raspi15 & USB stick
# had to take the : out of the hour:minute and replace with - because USB stick is formatted for FAT32
mysqldump -u robin -pMicr0s0ft mediadb | gzip > /home/robin/mediadb_backup/mediadb_backup.`date +%F-%H-%M`.sql.gz
#mysqldump -u robin -pMicr0s0ft mediadb | gzip > /media/usb/mediadb_backup/mediadb_backup.`date +%F.%H:%M`.sql.gz

# mysqldump to house_stats folder on raspi15 & USB stick
# had to take the : out of hour:minute and replace with - because USB stick is formatted for FAT32
mysqldump -u robin -pMicr0s0ft house_stats | gzip > /home/robin/house_stats_backup/house-stats-backup.`date +%F-%H-%M`.sql.gz
#mysqldump -u robin -pMicr0s0ft house_stats | gzip > /media/usb/house_stats_backup/house-stats-backup.`date +%F.%H:%M`.sql.gz

#mysqldump -u robin -pMicr0s0ft house_stats | gzip > /media/usb/house_stats_backup/house-stats-backup.`date +%F-%H-%M`.sql.gz

#tar zcvf /home/robin/raspi15_backup/raspi15-var-www.`date +%F.%H:%M`.tar.gz

# copy OfficeTempBackup to USB stick
scp  /home/robin/OfficeTempBackup/`ls -tp /home/robin/OfficeTempBackup | grep -v /$ | head -1` /media/usb/OfficeTempBackup


#scp -q /home/robin/house_stats_backup/house-stats-backup.`date +%F.%H:%M`.sql.gz robin@192.168.200.14:/home/robin/house_stats_backup

scp  /home/robin/house_stats_backup/`ls -tp /home/robin/house_stats_backup | grep -v /$ | head -1` /media/usb/house_stats_backup
scp  /home/robin/house_stats_backup/`ls -tp /home/robin/house_stats_backup | grep -v /$ | head -1` robin@192.168.200.14:/home/robin/house_stats_backup
scp  /home/robin/house_stats_backup/`ls -tp /home/robin/house_stats_backup | grep -v /$ | head -1` robin@192.168.200.16:/home/robin/house_stats_backup


#scp -q /home/robin/house_stats_backup/house-stats-backup.`date +%F.%H:%M`.sql.gz robin@192.168.200.16:/home/robin/house_stats_backup

scp  /home/robin/mediadb_backup/`ls -tp /home/robin/mediadb_backup | grep -v /$ | head -1` /media/usb/mediadb_backup
scp  /home/robin/mediadb_backup/`ls -tp /home/robin/mediadb_backup | grep -v /$ | head -1` robin@192.168.200.14:/home/robin/mediadb_backup
scp  /home/robin/mediadb_backup/`ls -tp /home/robin/mediadb_backup | grep -v /$ | head -1` robin@192.168.200.16:/home/robin/mediadb_backup


#scp -q /home/robin/mediadb_backup/mediadb_backup.`date +%F.%H:%M`.sql.gz robin@192.168.200.14:/home/robin/mediadb_backup

# scp -q /home/robin/raspi15_backup/raspi15-var-www.`date +%F.%H:%M`.tar.gz robin@192.168.200.16:/home/robin/raspi15_backup

# scp -q /home/robin/raspi15_backup/raspi15-var-www.`date +%F.%H:%M`.tar.gz robin@192.168.200.14:/home/robin/raspi15_backup



