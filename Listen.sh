#!/bin/bash

echo "waiting"
#listen
hexinject -s -i wlan0 -c 1 -f "port 54321" > cap.hex
echo "gotcha"

#read to payload
python read.py > payloadO
echo "readed"

#dencode payload to dencoded
python dencode.py > dencoded

echo "done; output to dencoded"

echo "**payload"
cat payload
echo "**payloadI"
cat payloadI
echo "**key"
cat key
echo "**payloadO"
cat payloadO
echo "**dencoded"
cat dencoded

python tasks.py
