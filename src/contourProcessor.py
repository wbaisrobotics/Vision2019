
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
    # Return whether or not the contour fill is greater than the constant minimum
    return ((cv2.contourArea (contour)/(width * height)) > visionConstants.minRectFill)

# Finds and analyzes the contours in the given frame (fitlered frame)
def findTarget (frame):

    # Run the opencv findContours method to find groups of white pixels
    im2, contours, hierarchy = cv2.findContours (frame, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    # Save only the contours that pass the minimum area test
    minAreaList = [x for x in contours if passesMinimumArea (x)]
           
    # Save only the contours that pass the minimum fill test
    minFillList = [x for x in minAreaList if passesMinimumRectFill (x)]
    
    # Calculate the bounding rects for the final contours
    boundingRects = [getMinAreaRect(x) for x in minFillList]

    print (len(minFillList))

    return minFillList, boundingRects
