#!/bin/sh

#  copy.sh
#
#  Shell script for efficently copying necessary files onto the RPi
#
#  Created by Orian Leitersdorf on 1/17/19.
#  

sshpass -p "raspberry" scp /Users/orianleitersdorf/git/FIRST\ Deep\ Space/python-multiCameraServer/runCamera  pi@10.43.38.30:
sshpass -p "raspberry" -r scp /Users/orianleitersdorf/git/FIRST\ Deep\ Space/python-multiCameraServer/src  pi@10.43.38.30:
