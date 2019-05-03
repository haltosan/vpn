#!/bin/bash

#listen
hexinject -s -i wlan0 -c 1 -f "port 12345" > cap.hex

#read to payload
python read.py > payload

#dencode payload to dencoded
python dencode.py > dencoded

echo "done; output to dencoded"
