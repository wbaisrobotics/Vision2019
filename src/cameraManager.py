
## File managing the cameras associated with the program

# Import the constants for vision processing
import visionConstants

# Import cscore (FRC Library) for connecting more efficently to the streaming servers and cameras
from cscore import CameraServer, VideoSource

# Initializes and sets up the RPi camera
def initializeHatchVisionCap():
    
    # Print out statement for intializing the camera
    print("Starting Hatch Vision Camera")
    
    # Initialize camera
    camera = CameraServer.getInstance() \
        .startAutomaticCapture(name="Hatch Vision Camera", path="/dev/video0")

    # Sets the resolution of the camera
    camera.setResolution (visionConstants.width, visionConstants.height)
    # Sets the config JSON to that defined in visionConstants
    camera.setConfigJson(visionConstants.cameraPropertiesJSON);
    
    # Return the created camera
    return camera

# Init function for starting the cameras
def init():

    # Initialize and define the properties of the camera
    camera = initializeHatchVisionCap()

# Returns an image sink for processing frames from the hatch vision camera
def getHatchVisionCameraSink():
    # Get a CvSink that will capture images from the camera for processing
    return CameraServer.getInstance().getVideo()

# Returns a stream for sending processed hatch vision camera images
def getHatchVisionCameraStream():
    # Setup a CvSource. This will send images back to the computer
    return CameraServer.getInstance().putVideo("Hatch Vision Camera Stream", visionConstants.width, visionConstants.height)
