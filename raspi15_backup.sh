#!/bin/sh


# Probably have to run as root since we are tar'ing the /var/www directory
# Cannot copy over to .16 since we are running as root, not as robin, so chown & chgrp

tar zcvf /home/robin/raspi15_backup/raspi15-var-www.`date +%F.%H:%M`.tar.gz /var/www
chown robin /home/robin/raspi15_backup/raspi15-var-www.`date +%F.%H:%M`.tar.gz
chgrp robin /home/robin/raspi15_backup/raspi15-var-www.`date +%F.%H:%M`.tar.gz

# now we can copy over as robin rather than root
#scp -q /home/robin/raspi15_backup/raspi15-var-www.`date +%F.%H:%M`.tar.gz robin@192.168.200.16:/home/robin/raspi15_backup

