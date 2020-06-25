#!/bin/bash

# Print the temperature line to beacon01.txt for the aprx temperatures
# T#151,20.6,52.5,19.4,0,0,00000000


printf "T#100," > /home/robin/test.txt
cat /home/robin/CurrentHouseTemp >> /home/robin/test.txt
printf "," >> /home/robin/test.txt 
cat /home/robin/CurrentOutsideTemp >> /home/robin/test.txt
printf "," >> /home/robin/test.txt 
cat /home/robin/CurrentGarageTemp >> /home/robin/test.txt
printf ",0,0,00000000" >> /home/robin/test.txt
