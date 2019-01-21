#!/usr/bin/env python3
#----------------------------------------------------------------------------
# Copyright (c) 2018 FIRST. All Rights Reserved.
# Open Source Software - may be modified and shared by FRC teams. The code
# must be accompanied by the FIRST BSD license file in the root directory of
# the project.
#----------------------------------------------------------------------------

# Import OpenCV (cv2) libraries
import cv2
# Import Numpy library for more complex array operations
import numpy as np

# Import cscore (FRC Library) for connecting more efficently to the streaming servers
from cscore import CameraServer, VideoSource

# Import the constants for vision processing
import visionConstants

# Imports the file in control of the cameras
import cameraManager

# Import the network table manager
import networkTables

# Import the contour processor
import contourProcessor

# Filters for the HSV range given in visionConstants
def filterHSV (frame):
    # Defines the lower range from the variables
    lowRange = (visionConstants.hueLow, visionConstants.satLow, visionConstants.valLow)
    # Defines the higher range from the variables
    highRange = (visionConstants.hueHigh, visionConstants.satHigh, visionConstants.valHigh)
    # Returns only the pixels within that range
    return cv2.inRange(hsvFrame, lowRange, highRange);

# Initializes the camera manager
cameraManager.init()

# Initializes the network tables
networkTables.init()

# Gets a sink for processing frames from the pi camera
cvSink = cameraManager.getPiCameraSink()

# Gets a source for sending frames back to the dashboard
outputStream = cameraManager.getPiCameraStream()

# Preallocate the image size before the loop ((rows, cols, depth), type)

frame = np.zeros(shape=(visionConstants.height, visionConstants.width, 3), dtype=np.uint8)

# Indefinetely (change this to be a signal from nt tables)
while True:
    
    # Grab a frame from the camera, returning the time of capture and the frame
    time, frame = cvSink.grabFrame(frame)
    # If error happened,
    if time == 0:
        # Send the output the error.
        print(cvSink.getError());
        # Skip the rest of the current iteration
        continue

    # Convert the image to HSV for easier filtering
    hsvFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Filter the image to only a range of HSV values
    rangedFrame = filterHSV (hsvFrame);

    # Find the target in the image
    contours, rects = contourProcessor.findTarget (rangedFrame);

    # Draw the bounding rects
    boxes = [np.int0(cv2.boxPoints (x)) for x in rects]
    cv2.drawContours (frame, boxes, -1, (0, 255, 0), 3)

    for contour in contours:

        # Get the properties of the minimum area rectangle
#(x, y), (width, height), angle = rect

        M = cv2.moments(contour)

        cX = int (M["m10"] / M["m00"])
        cY = int (M["m01"] / M["m00"])

        cv2.line (frame, (cX, cY), (int(visionConstants.width/2), int(visionConstants.height/2)), (255, 0, 0), 3)



    # Get the properties of the minimum area rectangle
#(x, y), (width, height), angle =

    # Draw lines to the centers of the contours


    
    # Send the result back to the driver station
    outputStream.putFrame(frame)

    # Update network table settings
    networkTables.update();
