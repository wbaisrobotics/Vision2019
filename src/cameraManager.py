
## File managing the cameras associated with the program

# Import the constants for vision processing
import visionConstants

# Initializes and sets up the RPi camera
def initializeRPiCap():
    
    # Print out statement for intializing the camera
    print("Starting RPI Camera")
    
    # Initialize camera
    camera = CameraServer.getInstance() \
        .startAutomaticCapture(name="Pi Camera", path="/dev/video0")

    # Sets the resolution of the camera
    camera.setResolution (visionConstants.width, visionConstants.height)
    # Sets the config JSON to that defined in visionConstants
    camera.setConfigJson(visionConstants.cameraPropertiesJSON);
    
    # Return the created camera
    return camera

# Init function for starting the cameras
def init():

    # Initialize and define the properties of the camera
    camera = initializeRPiCap()

# Returns an image sink for processing frames from the pi camera
def getPiCameraSink():
    # Get a CvSink that will capture images from the camera for processing
    return CameraServer.getInstance().getVideo()

# Returns a stream for sending processed pi camera images
def getPiCameraStream():
    # Setup a CvSource. This will send images back to the computer
    outputStream = CameraServer.getInstance().putVideo("Pi Camera", visionConstants.width, visionConstants.height)
