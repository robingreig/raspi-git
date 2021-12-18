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
/home/robin/raspi-git/SMSDatabase/dailyBackup.py
mv /home/robin/makerspace_backup.db /home/robin/backups/makerspace_backup_`date +%F`.db


