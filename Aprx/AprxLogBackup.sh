#!/bin/bash

# Needs to be run with sudo because it is log files

mv /var/log/aprx/aprx-rf.log /var/log/aprx/aprx-rf.log.$(date +%F_%R)
