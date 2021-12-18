#!/bin/sh

# Test with local file save
#newdate=`date -I`
#mysqldump -u root -pMicr0s0ft house_stats | gzip > /home/robin/house_stats-backup.$newdate.sql.gz

# Use ssh to transfer backup file to raspi11

# mysqldump to mediadb backup on raspi15 & USB stick
# had to take the : out of the hour:minute and replace with - because USB stick is formatted for FAT32

# Including hour & minute
#mysqldump -u robin -pMicr0s0ft makerspace | gzip > /home/robin/mariadb/makerspace_backup.`date +%F-%H-%M`.sql.gz

# NOT Including hour & minute
mysqldump -u robin -pMicr0s0ft makerspace | gzip > /home/robin/mariadb/makerspace_backup.`date +%F`.sql.gz


#mysqldump -u robin -pMicr0s0ft mediadb | gzip > /media/usb/mediadb_backup/mediadb_backup.`date +%F.%H:%M`.sql.gz

#tar zcvf /home/robin/raspi15_backup/raspi15-var-www.`date +%F.%H:%M`.tar.gz

# Copy backup to raspi20 Including hour & minute
#scp /home/robin/mariadb/makerspace_backup.`date +%F-%H-%M`.sql.gz robin@raspi20.hopto.org:/home/robin/mariadb/

# Copy backup to raspi20 NOT Including hour & minute
scp /home/robin/mariadb/makerspace_backup.`date +%F`.sql.gz robin@raspi20.hopto.org:/home/robin/mariadb/

# Copy backup to SMStest NOT Including hour & minute
###scp /home/robin/mariadb/makerspace_backup.`date +%F`.sql.gz robin@10.248.128.5:/home/robin/mariadb/
scp /home/robin/mariadb/makerspace_backup.`date +%F`.sql.gz robin@10.248.128.29:/home/robin/mariadb/



