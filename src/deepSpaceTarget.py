
# Import opencv libraries
import cv2

class DeepSpaceTarget:

    # Initializes given two rectangles for the target (in no specific order)
    def __init__(self, rect1, rect2):
        
        # Get the properties of the minimum area rectangle for the first rectangle
        (rect1X, rect1Y), (rect1Width, rect1Height), rect1Angle = rect1;
        
        # Get the properties of the minimum area rectangle for the second rectangle
        (rect1X, rect1Y), (rect1Width, rect1Height), rect1Angle = rect2;
        
        # Figure out which one is left and which is right
        if (rect1X < rect2X):
            self.lectRect = rect1;
            self.rightRect = rect2;
        else:
            self.lectRect = rect2;
            self.rightRect = rect1;
        self.lectRect = leftRect
        self.rightRect = rightRect

