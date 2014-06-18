#!/usr/bin/env python

import os

from subprocess import call
call(["ls", "-l"])

os.system("uptime | mail -s 'dms uptime' robin.greig@calalta.com")

