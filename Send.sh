#!/bin/bash

#encode payload with key to payload
python encode.py > payload
echo "encoded"

#make packet
python craft.py
echo "crafted"

IFS=" "
i=$(sed -n 5p config)
read -ra INT <<< "$i"
int=${INT[1]}
echo "int"
echo $int

#send
cat werk.pcap | hex2raw -r | hexinject -p -i $int
echo "sent"
echo " "
echo "**payload"
cat payload
echo "**payloadI"
cat payloadI
echo "**key"
cat key
