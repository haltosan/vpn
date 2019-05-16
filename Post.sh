#!/bin/bash

echo "What site do you want?"
read site
echo "What data do you want?"
read data
python post.py $site $data > payloadI
python sanitize.py
./Send.sh
sleep 1
./Listen.sh
