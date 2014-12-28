#!/bin/sh


# 2014.12.28 Changed date in filename to remove colons for FAT32 usb stick

# Probably have to run as root since we are tar'ing the /var/www directory
# Cannot copy over to .16 since we are running as root, not as robin, so chown & chgrp

#tar zcvf /home/robin/raspi15_www_backup/raspi15-var-www.`date +%F.%H:%M`.tar.gz /var/www
#chown robin /home/robin/raspi15_www_backup/*
#chgrp robin /home/robin/raspi15_www_backup/*

# Have to put it in the /home directory since it is a full backup of robin directory
tar zcvf /home/raspi15-home-dir.`date +%F-%H-%M`.tar.gz /home/robin
chown robin /home/raspi15-home-dir*
chgrp robin /home/raspi15-home-dir*

# now we can copy over as robin rather than root
#scp -q /home/`ls -tp /home/ | grep -v /$ | head -1` robin@192.168.200.14:/home/robin/raspi15_backup
#scp -q /home/`ls -tp /home/ | grep -v /$ | head -1` robin@192.168.200.14:/home/robin/raspi15_backup

# Gives error if trying to copy over as robin not root
# Solution is to run the backup as root and the copy as robin
#scp -q /home/`ls -tp /home/ | grep -v /$ | head -1` robin@192.168.200.14:/home/robin/raspi15_backup
#scp -q /home/`ls -tp /home/ | grep -v /$ | head -1` robin@192.168.200.16:/home/robin/raspi15_backup

