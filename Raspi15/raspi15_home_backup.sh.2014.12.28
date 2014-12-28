#!/bin/sh


# raspi15_backup runs as sudo to properly backup complete home directory
# running this copy to .14 & .16 as robin
scp -q /home/`ls -tp /home/ | grep -v /$ | head -1` robin@192.168.200.14:/home/robin/raspi15_backup
scp -q /home/`ls -tp /home/ | grep -v /$ | head -1` robin@192.168.200.16:/home/robin/raspi15_backup

