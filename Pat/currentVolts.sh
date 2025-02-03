#!/bin/bash

printf 'The Garage Solar Battery Voltage is: ' > /home/robin/test_file.txt
cat /home/robin/CurrentAdc0Volts >> /home/robin/test_file.txt
printf '\n' >> /home/robin/test_file.txt
printf '\nAnd the Garage Battery Voltage is: ' >> /home/robin/test_file.txt
cat /home/robin/CurrentAdc1Volts >> /home/robin/test_file.txt
printf '\n' >> ./test_file.txt



