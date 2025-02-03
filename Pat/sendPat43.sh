#!/bin/bash

#echo "Sending text from mqtt43" | pat compose VE6RBN -s BashTest robin.greig@sait.ca
cat /home/robin/test_file.txt | pat compose VE6RBN -s 'Solar Battery Voltage' robin.greig@sait.ca

pat connect telnet
