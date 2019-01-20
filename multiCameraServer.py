#!/usr/bin/env python3
#----------------------------------------------------------------------------
# Copyright (c) 2018 FIRST. All Rights Reserved.
# Open Source Software - may be modified and shared by FRC teams. The code
# must be accompanied by the FIRST BSD license file in the root directory of
# the project.
#----------------------------------------------------------------------------

import json
import time
import sys
import cv2
import numpy as np

from cscore import CameraServer, VideoSource
from networktables import NetworkTablesInstance

# Initializes and sets up the RPi camera
def initializeRPiCap():
    
    # Initialize on port 0
    cap = cv2.VideoCapture(0)

    cap.set(10, 0.3)

    return cap

# Captures an image from the cap if the capture is open
def captureImage(cap):
    if (cap.isOpened()):
        ret, frame = cap.read()
        if (ret):
            return frame

def



cs = CameraServer.getInstance()

# Setup a CvSource. This will send images back to the Dashboard
outputStream = cs.putVideo("Cam1", 640, 480)

# start NetworkTables
ntinst = NetworkTablesInstance.getDefault()
ntinst.startClientTeam(4338)

# Capture frame-by-frame
ret, frame = cap.read()

# Run forever
while (True):

    # Capture the frame
    frame = captureImage (cap);
    
    hsvImage = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    rangedImage = cv2.inRange(hsvImage, np.array([0, 0, 50]), np.array([180, 255, 255]))

    # (optional) send some image back to the dashboard
    outputStream.putFrame(rangedImage)
