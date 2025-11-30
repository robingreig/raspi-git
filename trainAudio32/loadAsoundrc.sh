#!/bin/bash

sleep 15

cp /home/robin/raspi-git/trainAudio32/asoundrc /home/robin/.asoundrc
aplay /home/robin/TrainHorn01.wav
