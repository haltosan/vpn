#!/bin/bash

echo "waiting"
IFS=" "
i=$(sed -n 5p config)
read -ra INT <<< "$i"
int=${INT[1]}
IFS=" "
j=$(sed -n 1p config)
read -ra LHOST <<< "$j"
lhost=${LHOST[1]}
IFS=" "
k=$(sed -n 3p config)
read -ra RHOST <<< "$k"
rhost=${RHOST[1]}
echo "int, lhost, rhost"
echo $int
echo $lhost
echo $rhost
#listen
hexinject -s -i $int -c 1 -f "port 12345"> cap.hex
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

echo "started tasks"
python tasks.py
