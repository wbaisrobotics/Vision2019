
# Import OpenCV (cv2) libraries
import cv2

# Import the vision constants for filtering
import visionConstants

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
    print ((cv2.contourArea (contour)/(width * height)))
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
    # Represents the smallest error to date as running the iterations (1000 to gurantee the default will be replaced)
    smallestError = 1000
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
    print ("The smallest angle error was: %d, at index1: %d & index2: %d" % (smallestError, smallestErrorIndex1, smallestErrorIndex2))
