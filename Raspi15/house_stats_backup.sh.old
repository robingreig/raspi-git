#!/bin/sh

# Test with local file save
#newdate=`date -I`
#mysqldump -u root -pMicr0s0ft house_stats | gzip > /home/robin/house_stats-backup.$newdate.sql.gz

# Use ssh to transfer backup file to raspi11

mysqldump -u robin -pMicr0s0ft mediadb | gzip > /home/robin/mediadb_backup/mediadb_backup.`date +%F.%H:%M`.sql.gz

mysqldump -u robin -pMicr0s0ft house_stats | gzip > /home/robin/house_stats_backup/house-stats-backup.`date +%F.%H:%M`.sql.gz

#tar zcvf /home/robin/raspi15_backup/raspi15-var-www.`date +%F.%H:%M`.tar.gz

scp -q /home/robin/house_stats_backup/house-stats-backup.`date +%F.%H:%M`.sql.gz robin@192.168.200.16:/home/robin/house_stats_backup

scp -q /home/robin/house_stats_backup/house-stats-backup.`date +%F.%H:%M`.sql.gz robin@192.168.200.14:/home/robin/house_stats_backup

scp -q /home/robin/mediadb_backup/mediadb_backup.`date +%F.%H:%M`.sql.gz robin@192.168.200.16:/home/robin/mediadb_backup

scp -q /home/robin/mediadb_backup/mediadb_backup.`date +%F.%H:%M`.sql.gz robin@192.168.200.14:/home/robin/mediadb_backup

# scp -q /home/robin/raspi15_backup/raspi15-var-www.`date +%F.%H:%M`.tar.gz robin@192.168.200.16:/home/robin/raspi15_backup

# scp -q /home/robin/raspi15_backup/raspi15-var-www.`date +%F.%H:%M`.tar.gz robin@192.168.200.14:/home/robin/raspi15_backup



