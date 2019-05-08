#!/bin/bash

echo "What site do you want?"
python siteCraft.py > payloadI
python sanitize.py
echo "san-ed"
./Send.sh
sleep 1
./Listen.sh
