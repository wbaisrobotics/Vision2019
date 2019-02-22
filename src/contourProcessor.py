
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
def findDeepSpaceTarget (boundingRects):
    
    ## Define variables for finding the pair with the smallest error
    # Represents the smallest error to date as running the iterations (10000 to gurantee the default will be replaced)
    smallestError = 10000
    # The index of the first rectangle in the pair of rectangles with the smallestError
    smallestErrorIndex1 = -1
    # The index of the second rectangle in the pair of rectangles with the smallestError
    smallestErrorIndex2 = -1

    ## Iterate through each pair of bounding rects
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

            # Cacluate the error for the angle between them and the given field angle
            error = visionConstants.targetAngle - (angle2 - angle1)

            # If this error is smaller than all those before
            if (error < smallestError):
                ## then remember these indices
                # Save the index for the first one
                smallestErrorIndex1 = index1
                # Save the index for the second one
                smallestErrorIndex2 = index2
                # Save the error for future calculations
                smallestError = error

    # Print out the results
#    print ("The smallest angle error was: %d, at index1: %d & index2: %d" % (smallestError, smallestErrorIndex1, smallestErrorIndex2))

    # Make sure it found something
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

    # Compute the oi-ratio
    outerDistance = (rightX + float(rightWidth)/2) - (leftX - float(leftWidth)/2);
    innerDistance = (rightX - float(rightWidth)/2) - (leftX + float(leftWidth)/2);
    oiRatio = float (outerDistance)/innerDistance;

    # Return the results
    return averageX, averageY, outerDistance/visionConstants.width, oiRatio;

# Calculates the differences relative to the width and height of the screen
# (returning xDiff in range [-1 (full left) 1 (full right)] and yDiff in range [-1 (full down) 1 (full up)])
def calculateTargetDifferences (x, y):

    # Calculate the x difference (converting to [-1 1] setup)
    xDiff = (x - (visionConstants.width/2)) / (visionConstants.width/2);
    # Calculate the y difference (converting to [-1 1] setup)
    yDiff = (y - (visionConstants.height/2)) / (visionConstants.height/2);

    # Return calculated values
    return xDiff, yDiff;

# Compute real-world distances/angles based on the rectangles
#def compute_output_values(leftRect, rightRect, centerX, centerY):
#
#    # Calculate the left verticies
#    leftVerticies = cv2.boxPoints(leftRect);
#    # Calculate the right verticies
#    rightVerticies = cv2.boxPoints(rightRect);
#
#    # Combine the left and right into one verticies array
#    image_points = np.concatenate((leftVerticies, rightVerticies));
#    image_points[:,0] -= (centerX);
#    image_points[:,1] -= (centerY);
#    image_points[:,1] *= -1;
#    print (image_points);
#    print (visionConstants.model_points);
#
#    # Compute robot orientation
#    (ret, rvec, tvec) = cv2.solvePnP (visionConstants.model_points, image_points, visionConstants.mat, visionConstants.dist_coeffs);
#
#    # Compute the necessary output distance and angles
#    x = tvec[0][0]
#    y = tvec[1][0]
#    z = tvec[2][0]
#    # distance in the horizontal plane between camera and target
#    distance = math.sqrt(x**2 + z**2)
#    # horizontal angle between camera center line and target
#    angle1 = math.atan2(x, z)
#    rot, _ = cv2.Rodrigues(rvec)
#    rot_inv = rot.transpose()
#    pzero_world = np.matmul(rot_inv, -tvec)
#    angle2 = math.atan2(pzero_world[0][0], pzero_world[2][0])
#    print ("Distance: %f, Angle1: %f, Angle2: %f, X: %f, Y: %f, Z: %f, CenterY: %f" % (distance, angle1, angle2, x, y, z, centerY));
#    return distance, angle1, angle2
