#!/bin/bash

python craft.py
./send.sh
sleep .5
./cap.sh
python read.py > payload
python dencode.py > payload
#python craft.py
#timeout .3s bash transfer.sh
#nano translated
nano payload
