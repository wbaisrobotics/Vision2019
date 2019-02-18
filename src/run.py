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

import datetime

def drawPoint(p):
    cv2.circle(rangedFrame, (p[0], p[1]), 10, (255, 255, 0), 3);
    return 0;

# Filters for the HSV range given in visionConstants
def filterHSV (frame):
    # Defines the lower range from the variables
    lowRange = (visionConstants.hueLow, visionConstants.satLow, visionConstants.valLow)
    # Defines the higher range from the variables
    highRange = (visionConstants.hueHigh, visionConstants.satHigh, visionConstants.valHigh)
    # Returns only the pixels within that range
    return cv2.inRange(frame, lowRange, highRange);

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
while visionConstants.run:

    start = datetime.datetime.now();

    # Grab a frame from the camera, returning the time of capture and the frame
    time, frame = cvSink.grabFrame(frame)
    # If error happened,
    if time == 0:
        # Send the output the error.
        print(cvSink.getError());
        # Skip the rest of the current iteration
        continue

    afterFrameGrab = datetime.datetime.now();

    # Convert the image to HSV for easier filtering
#    hsvFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    afterHSVConversion = datetime.datetime.now();

    # Filter the image to only a range of HSV values
    rangedFrame = filterHSV (frame);

    afterRange = datetime.datetime.now();

    # Find the rectangular targets in the image
    contours, rects = contourProcessor.findRectangles (rangedFrame);

    afterFindRectangles = datetime.datetime.now();

    # Draw the bounding rects
    boxes = [np.int0(cv2.boxPoints (x)) for x in rects]
    cv2.drawContours (frame, boxes, -1, (0, 255, 0), 3)

    # Draw the lines to the rects
    for rect in rects:

        (cX, cY), (width1, height1), angle1 = rect

        cv2.line (frame, (int(cX), int(cY)), (int(visionConstants.width/2), int(visionConstants.height/2)), (255, 0, 0), 3)

    # Attempts to locate a FIRST Deep Space Game Target
    leftRect, rightRect = contourProcessor.findDeepSpaceTarget(rects);

    afterFindTarget = datetime.datetime.now();

#    # If target was found
#    if (leftRect != -9999):
#
#        # Draw line to center of FIRST Deep Space target
#        cv2.line (frame, (targetX, targetY), (int(visionConstants.width/2), int(visionConstants.height/2)), (0, 255, 0), 3)
#
#        # Calculate the x and y differences relative to the screen
#        xDiff, yDiff = contourProcessor.calculateTargetDifferences(targetX, targetY);
#
#        # Immediately send the difference values through the network tables
#        networkTables.sendTargetData (xDiff, yDiff, targetAngle, 0);
#
#    # If target not found
#    if (targetX == -9999):
#
#        # Immediately send the error values through the network tables
#        networkTables.sendTargetData (-9999, -9999, -9999, -9999);

    if (leftRect != -9999):

        # Calculate the left verticies
        leftVerticies = cv2.boxPoints(leftRect);
        # Calculate the right verticies
        rightVerticies = cv2.boxPoints(rightRect);

        # Combine the left and right into one verticies array
        image_points = np.concatenate((leftVerticies, rightVerticies));

        np.apply_along_axis(drawPoint, axis=1, arr=image_points);


    # Send the result back to the driver station
    outputStream.putFrame(rangedFrame);

    # Update network table settings
    networkTables.update();

    end = datetime.datetime.now();

    frameGrabTime = (afterFrameGrab - start).microseconds / 1000;
    hsvConversionTime = (afterHSVConversion-afterFrameGrab).microseconds / 1000;
    rangeTime = (afterRange - afterHSVConversion).microseconds / 1000;
    findRectTime = (afterFindRectangles - afterRange).microseconds / 1000;
    findTargetTime = (afterFindTarget - afterFindRectangles).microseconds / 1000;
    endTime = (end - afterFindTarget).microseconds / 1000;

    print ("Time Report - Frame Grab: %d, HSV Conversion: %d, Range: %d, Find Rectangles: %d, Find Target: %d, End: %d" % (frameGrabTime, hsvConversionTime, rangeTime, findRectTime, findTargetTime, endTime));
