#!/bin/bash

echo "What site do you want?"
python siteCraft.py > payloadI
./Send.sh
sleep 1
./Listen.sh
