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

import visionConstants

from cscore import CameraServer, VideoSource
from networktables import NetworkTablesInstance

# Initializes and sets up the RPi camera
def initializeRPiCap():
    
    # Print out statement for intializing the camera
    print("Starting RPI Camera")
    
    # Initialize camera
    camera = CameraServer.getInstance() \
        .startAutomaticCapture(name="Pi Camera", path="/dev/video0")

    # Sets the resolution of the camera
    camera.setResolution (visionConstants.width, visionConstants.height)
    # Sets the config JSON to that defined in constants
    camera.setConfigJson(visionConstants.cameraPropertiesJSON);

    return camera

# Captures an image from the cap if the capture is open
def captureImage(cap):
    if (cap.isOpened()):
        ret, frame = cap.read()
        if (ret):
            return frame

# Initialize and define the properties of the camera
camera = initializeRPiCap()

# Get a CvSink. This will capture images from the camera
cvSink = CameraServer.getInstance().getVideo()

# Setup a CvSource. This will send images back to the computer
outputStream = CameraServer.getInstance().putVideo("Name", visionConstants.width, visionConstants.height)

# Preallocate the image size before the loop ((rows, cols, depth), type)
img = np.zeros(shape=(visionConstants.height, visionConstants.width, 3), dtype=np.uint8)

# Indefinetely (change this to be a signal from nt tables)
while True:
    # Grab a frame from the camera, returning the time of capture and the frame
    time, frame = cvSink.grabFrame(img)
    # If error happened,
    if time == 0:
        # Send the output the error.
        print(cvSink.getError());
        # Skip the rest of the current iteration
        continue

    # Convert the image to HSV for easier filtering
    hsvFrame = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    # Filter the image to only a range of HSV values
    rangedFrame = cv2.inRange(hsvFrame, (0, 0, 30), (180, 255, 255))
    
    # (optional) send some image back to the dashboard
    outputStream.putFrame(rangedFrame)
