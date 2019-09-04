#!/bin/bash
# Script: my-pi-temp.sh
# Purpose: Display the ARM CPU and GPU temp of the Raspiberry Pi
cpu=$(</sys/class/thermal/thermal_zone0/temp)
echo "$(date) @ $(hostname)"
echo "----------------------"
echo "GPU => $(/opt/vc/bin/vcgencmd measure_temp)"
echo "CPU => $((cpu/1000))'C"

