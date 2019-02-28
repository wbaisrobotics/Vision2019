
# Import OpenCV (cv2) libraries
import cv2

# Import the vision constants for filtering
import visionConstants

# Import numpy for matrix manipulation
import numpy as np

# Import math
import math

# Whether or not the given contour passes the minimum area test
def passesMinimumArea(contour):
    # Return whether or not the contour area is greater than the constant minimum
    return (cv2.contourArea (contour) > visionConstants.minArea)

# Calculates the minimum area rectangle (tilted) of the contour
def getMinAreaRect(contour):
    # Returns the minimum area rectangle of the contour
    return cv2.minAreaRect (contour)

# Whether or not the given contour passes the minimum rectangle fill test (contourArea / minBoundingRectArea) > constant
def passesMinimumRectFill(contour):
    # Get the properties of the minimum area rectangle
    (x, y), (width, height), angle = getMinAreaRect(contour)
#    print ((cv2.contourArea (contour)/(width * height)))
    # Return whether or not the contour fill is greater than the constant minimum
    return ((cv2.contourArea (contour)/(width * height)) > visionConstants.minRectFill)

# Finds and analyzes the contours in the given frame (fitlered frame)
def findRectangles (frame):

    # Run the opencv findContours method to find groups of white pixels
    im2, contours, hierarchy = cv2.findContours (frame, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    # Save only the contours that pass the minimum area test
    minAreaList = [x for x in contours if passesMinimumArea (x)]
           
    # Save only the contours that pass the minimum fill test
    minFillList = [x for x in minAreaList if passesMinimumRectFill (x)]
    
    # Calculate the bounding rects for the final contours
    boundingRects = [getMinAreaRect(x) for x in minFillList]

    # Returns the contours that have passes the filters and the cooresponding bounding rects
    return minFillList, boundingRects

# Finds the FIRST Deep Space vision target amongst independent bounding rectangular
# Considers the possibility for multiple targets to be in sight, and implements various methods to choose
# the target closest to the center of the screen
def findDeepSpaceTarget (boundingRects):
    
    ## Define variables for finding the pair with the smallest error
    # Represents the smallest error to date as running the iterations (10000 to gurantee the default will be replaced)
    smallestError = 10000
    # The index of the first rectangle in the pair of rectangles with the smallestError
    smallestErrorIndex1 = -1
    # The index of the second rectangle in the pair of rectangles with the smallestError
    smallestErrorIndex2 = -1

    # Iterate through each pair of bounding rects
    for index1, rect1 in enumerate (boundingRects):

        # Get the properties of the minimum area rectangle for rect1
        (x1, y1), (width1, height1), angle1 = rect1

        # Iterate through each other pair
        for index2, rect2 in enumerate (boundingRects):

            # If rect1==rect2
            if (index2 == index1):
                continue;

            # Get the properties of the minimum area rectangle for rect2
            (x2, y2), (width2, height2), angle2 = rect2
            
            ## Angle test (to make sure the contours found are in fact the deep space reflective targets)
            
            # If rect 1 is the left rectangle
            if (x1 < x2):
                angleL = angle1;
                angleR = angle2;
                    
            # If rect 2 is the left rectangle
            if (x2 <= x1):
                angleL = angle2;
                angleR = angle1;

            # Cacluate the angle error for the angle between them and the given field angle
            angleError = abs(visionConstants.targetAngle - ((90-abs(angleL)) + abs(angleR)));
            
            print ("AngleL: %d, AngleR: %d, Error: %d" % (angleL, angleR, angleError));

            # If this angle error is acceptable (within the error specified in vision constants)
            if (angleError < visionConstants.targetAngleError):
                
                
                ## Target ratio test (to make sure the two rectangles belong to the same target - two rects from different targets would have a significantly larger ratio)
                
                # Calculate the target ratio error (width / average height)
                targetRatioError = abs(abs((x1 - x2) / ((height1 + height2)/2)) - visionConstants.targetRatio);
                
                print (targetRatioError);
                
                # And the target ratio is acceptable
                if (targetRatioError < visionConstants.targetRatioError):
                    
                    
                    ## Find the target closest to the center of the screen and follow that one
                    
                    # Calculate distance to center of screen from center of target (in order to use the target closest to middle)
                    distanceToCenter = abs(((x1 + x2)/2) - (visionConstants.width/2));

                    # And this target has a closer distance to the center than the one before it
                    if (distanceToCenter < smallestError):
                        
                        # TEMPORARY PRINT for testing
                        print ("Replaced previous record. Data - angleError: %d, targetRatioError: %d, distanceToCenter: %d, previousDistanceToCenter: %d" % (angleError, targetRatioError, distanceToCenter, smallestError));
                        
                        ## then remember these indices
                        
                        # Save the index for the first one
                        smallestErrorIndex1 = index1
                        # Save the index for the second one
                        smallestErrorIndex2 = index2
                        # Save the error for future calculations
                        smallestError = distanceToCenter
                    
                    
                

    # If it did not find the target
    if (smallestError == 10000):

        # Log the error
        print ("DEEP Space Target not found")

        # Return error values
        return -9999, -9999, -9999, -9999;


    # Get the properties of the minimum area rectangle for the first selected rectangle
    (rect1X, rect1Y), (rect1Width, rect1Height), rect1Angle = boundingRects [smallestErrorIndex1];

    # Meaning necessary to swap width and height (given DEEP SPACE dimensions)
    if (rect1Width > rect1Height):
        t = rect1Width ;
        rect1Width = rect1Height;
        rect1Height = t;

    # Get the properties of the minimum area rectangle for the second selected rectangle
    (rect2X, rect2Y), (rect2Width, rect2Height), rect2Angle = boundingRects [smallestErrorIndex2];

    # Meaning necessary to swap width and height (given DEEP SPACE dimensions)
    if (rect2Width > rect2Height):
        t = rect2Width ;
        rect2Width = rect2Height;
        rect2Height = t;

    # Calculate the average values for x, y, & angle
    averageX = int((rect1X + rect2X)/2);
    averageY = int((rect1Y + rect2Y)/2);
    averageAngle = int((rect1Angle + rect2Angle)/2);
    
#    print ("Rect1X: %d, Rect1Width: %d, Rect1Height: %d, Rect2X: %d, Rect2Width: %d" % (rect1X, rect1Width, rect1Height, rect2X, rect2Width));

    # Log the result
    print ("The center x: %d, y: %d, angle: %d" % (averageX, averageY, averageAngle));

    # If rect 1 is the left rectangle
    if (rect1X < rect2X):
        # Store rect 1 as the left rect
        leftRect = boundingRects [smallestErrorIndex1];
        # Save the properties for left rect
        leftX = rect1X;
        leftY = rect1Y;
        leftWidth = rect1Width;
        leftHeight = rect1Height;
        leftAngle = rect1Angle;
        # Store rect 2 as the left rect
        rightRect = boundingRects [smallestErrorIndex2];
        # Save the properties for right rect
        rightX = rect2X;
        rightY = rect2Y;
        rightWidth = rect2Width;
        rightHeight = rect2Height;
        rightAngle = rect2Angle;

    # If rect 2 is the left rectangle
    if (rect2X <= rect1X):
        # Store rect 2 as the left rect
        leftRect = boundingRects [smallestErrorIndex2];
        # Save the properties for left rect
        leftX = rect2X;
        leftY = rect2Y;
        leftWidth = rect2Width;
        leftHeight = rect2Height;
        leftAngle = rect2Angle;
        # Store rect 1 as the left rect
        rightRect = boundingRects [smallestErrorIndex1];
        # Save the properties for right rect
        rightX = rect1X;
        rightY = rect1Y;
        rightWidth = rect1Width;
        rightHeight = rect1Height;
        rightAngle = rect1Angle;

    # Compute the height-ratio
    heightRatio = float (leftHeight)/rightHeight;

    # Compute the ttsr (target height to screen height ratio)
    ttsr = float ((leftHeight+rightHeight)/2) / visionConstants.height;

    # Return the results
    return averageX, averageY, heightRatio, ttsr;

# Calculates the differences relative to the width and height of the screen
# (returning xDiff in range [-1 (full left) 1 (full right)] and yDiff in range [-1 (full down) 1 (full up)])
def calculateTargetDifferences (x, y):

    # Calculate the x difference (converting to [-1 1] setup)
    xDiff = (x - (visionConstants.width/2)) / (visionConstants.width/2);
    # Calculate the y difference (converting to [-1 1] setup)
    yDiff = (y - (visionConstants.height/2)) / (visionConstants.height/2);

    # Return calculated values
    return xDiff, yDiff;
