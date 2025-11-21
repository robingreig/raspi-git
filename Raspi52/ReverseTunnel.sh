#!/bin/bash

#nohup ssh -f -N -T -R22201:localhost:22 raspi15.hopto.org
#autossh -f -N -T -R22201:localhost:22 raspi20.hopto.org
#autossh -f -M 0 -N -T -o "ServerAliveInterval 120" -R22201:localhost:22 raspi20.hopto.org
#autossh -f -M 0 -N -T -o "ServerAliveInterval 120" -o "ExitOnForwardFailure=yes" -R22201:localhost:22 raspi20.hopto.org
autossh -f -M 0 -N -T -o "ServerAliveInterval 180" -o "ExitOnForwardFailure=yes" -R22252:localhost:22 raspi20.hopto.org
