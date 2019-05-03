#!/bin/bash

cat werk.pcap | hex2raw -r | hexinject -p -i wlan0
