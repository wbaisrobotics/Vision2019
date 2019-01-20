#!/bin/sh

#  copy.sh
#  
#
#  Created by Orian Leitersdorf on 1/17/19.
#  

sshpass -p "raspberry" scp /Users/orianleitersdorf/git/FIRST\ Deep\ Space/python-multiCameraServer/runCamera  pi@10.43.38.30:
sshpass -p "raspberry" scp /Users/orianleitersdorf/git/FIRST\ Deep\ Space/python-multiCameraServer/multiCameraServer.py  pi@10.43.38.30:
