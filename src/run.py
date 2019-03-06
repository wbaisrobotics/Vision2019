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

# Import datetime for keeping track of time
import datetime

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

# Gets a sink for processing frames from the hatch vision camera
hatchSink = cameraManager.getHatchVisionCameraSink();
# Gets a sink for processing frames from the ball vision camera
ballSink = cameraManager.getBallVisionCameraSink();

# Gets a source for sending frames back to the dashboard
outputStream = cameraManager.getVisionStream()

# Preallocate the image size before the loop ((rows, cols, depth), type)
frame = np.zeros(shape=(visionConstants.height, visionConstants.width, 3), dtype=np.uint8)
# Preallocate the image size before the loop ((rows, cols, depth), type)
#hsvFrame = np.zeros(shape=(visionConstants.height, visionConstants.width, 3), dtype=np.uint8)

# While network tables indicate to run
while True:
    
#    if (visionConstants.run):
#
##        print ("LOW BRT");
#
#        cameraManager.lowBrtMode();
#
#        # Measure the time at start
#        start = datetime.datetime.now();
#
#        # If using the ball camera...
#        if (visionConstants.reverse):
#            # Grab a frame from the ball camera, returning the time of capture and the frame
#            time, frame = ballSink.grabFrame(frame)
#            # If error happened,
#            if time == 0:
#                # Output the error.
#                print(ballSink.getError());
#                # Update network table settings
#                networkTables.update();
#                # Skip the rest of the current iteration
#                continue
#        # If using the hatch camera
#        else:
#            # Grab a frame from the hatch camera, returning the time of capture and the frame
#            time, frame = hatchSink.grabFrame(frame)
#            # If error happened,
#            if time == 0:
#                # Output the error.
#                print(hatchSink.getError());
#                # Update network table settings
#                networkTables.update();
#                # Skip the rest of the current iteration
#                continue;
#
#        # Measure the time after grabbing the frame
#        afterFrameGrab = datetime.datetime.now();
#
#        # Convert the image to HSV for easier filtering
#        #    hsvFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
#
#        # Measure the time after HSV conversion
#        afterHSVConversion = datetime.datetime.now();
#
#        # Filter the image to only a range of values
#        rangedFrame = filterHSV (frame);
#
#        # Measure the time after ranging the image
#        afterRange = datetime.datetime.now();
#
#        # Find the rectangular targets in the image
#        contours, rects = contourProcessor.findRectangles (rangedFrame);
#
#        # Measure the time it took to find the rectangles
#        afterFindRectangles = datetime.datetime.now();
#
#        # Draw the bounding rects
#        boxes = [np.int0(cv2.boxPoints (x)) for x in rects]
#        cv2.drawContours (frame, boxes, -1, (0, 255, 0), 3)
#
#        # Draw the lines to the rects
#        for rect in rects:
#
#            # Get the information from the rect
#            (cX, cY), (width1, height1), angle1 = rect
#
#            # Draw a line to the rect center from the frame center
#            cv2.line (frame, (int(cX), int(cY)), (int(visionConstants.width/2), int(visionConstants.height/2)), (255, 0, 0), 3)
#
#        # Attempt to locate a DEEP Space target given the rectangles
#        targetX, targetY, heightRatio, ttsr = contourProcessor.findDeepSpaceTarget(rects);
#
#        # Measure the time after finding the deep space target
#        afterFindTarget = datetime.datetime.now();
#
#        # If target was found
#        if (targetX != -9999):
#
#            # Draw line to center of FIRST Deep Space target
#            cv2.line (frame, (targetX, targetY), (int(visionConstants.width/2), int(visionConstants.height/2)), (0, 255, 0), 3)
#
#            # Calculate the x and y differences relative to the screen
#            xDiff, yDiff = contourProcessor.calculateTargetDifferences(targetX, targetY);
#
#            # Immediately send the difference values through the network tables
#            networkTables.sendTargetData (xDiff, yDiff, heightRatio, ttsr);
#
#        # If target not found
#        if (targetX == -9999):
#
#            # Immediately send the error values through the network tables
#            networkTables.sendTargetData (-9999, -9999, -9999, -9999);
#
#        # Send the result back to the driver station
#        outputStream.putFrame(frame);
#
#        # Update network table settings
#        networkTables.update();
#
#        # Measure the time at the end
#        end = datetime.datetime.now();
#
#        # Calculate the times for each calculation
#        frameGrabTime = (afterFrameGrab - start).microseconds / 1000;
#        hsvConversionTime = (afterHSVConversion-afterFrameGrab).microseconds / 1000;
#        rangeTime = (afterRange - afterHSVConversion).microseconds / 1000;
#        findRectTime = (afterFindRectangles - afterRange).microseconds / 1000;
#        findTargetTime = (afterFindTarget - afterFindRectangles).microseconds / 1000;
#        endTime = (end - afterFindTarget).microseconds / 1000;
#
#        # Log the time stamps
#        print ("Time Report - Frame Grab: %d, HSV Conversion: %d, Range: %d, Find Rectangles: %d, Find Target: %d, End: %d" % (frameGrabTime, hsvConversionTime, rangeTime, findRectTime, findTargetTime, endTime));
#
#    else:

#        print ("HIGH BRT");

    cameraManager.highBrtMode();

    # Update network table settings
    networkTables.update();



