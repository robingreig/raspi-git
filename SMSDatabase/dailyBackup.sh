#!/bin/sh

# Use ssh to transfer backup file to raspi11

# Including hour & minute
#mysqldump -u robin -pMicr0s0ft makerspace | gzip > /home/robin/mariadb/makerspace_backup.`date +%F-%H-%M`.sql.gz

# NOT Including hour & minute
#mysqldump -u robin -pMicr0s0ft makerspace | gzip > /home/robin/mariadb/makerspace_backup.`date +%F`.sql.gz

# Copy backup to raspi20 NOT Including hour & minute
#scp /home/robin/mariadb/makerspace_backup.`date +%F`.sql.gz robin@raspi20.hopto.org:/home/robin/mariadb/

# Copy backup to SMStest NOT Including hour & minute
###scp /home/robin/mariadb/makerspace_backup.`date +%F`.sql.gz robin@10.248.128.5:/home/robin/mariadb/
#scp /home/robin/mariadb/makerspace_backup.`date +%F`.sql.gz robin@10.248.128.29:/home/robin/mariadb/

#  add timeOUT times for members who forgot to sign out
/home/robin/raspi-git/SMSDatabase/dayEnd.py

# backup sqlite3 database
/home/robin/raspi-git/SMSDatabase/dailyBackup.py

# zip the file
gzip /home/robin/makerspace_backup.db

# copy zipped backup to raspi20
scp /home/robin/makerspace_backup.db.gz robin@rlg.webhop.me:/home/robin/SMSDatabase/makerspace_backup_`date +%F`.db.gz

# move backup to /home//robin/backups
mv /home/robin/makerspace_backup.db.gz /home/robin/backups/makerspace_backup_`date +%F`.db.gz


