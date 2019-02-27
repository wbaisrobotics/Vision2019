
## File managing the cameras associated with the program

# Import the constants for vision processing
import visionConstants

# Import cscore (FRC Library) for connecting more efficently to the streaming servers and cameras
from cscore import CameraServer, VideoSource

# Initializes and sets up the Hatch Vision camera
def initializeHatchVisionCap():
    
    # Print out statement for intializing the camera
    print("Starting Hatch Vision Camera")
    
    # Initialize camera
    camera = CameraServer.getInstance() \
        .startAutomaticCapture(name="Hatch Vision Camera", path="/dev/v4l/by-path/platform-3f980000.usb-usb-0:1.2:1.0-video-index0")

    # Sets the resolution of the camera
    camera.setResolution (visionConstants.width, visionConstants.height)
    # Sets the config JSON to that defined in visionConstants
    camera.setConfigJson(visionConstants.cameraPropertiesJSON);
    
    # Return the created camera
    return camera

# Initializes and sets up the Hatch Driver camera
def initializeHatcherDriverCap():
    
    # Print out statement for intializing the camera
    print("Starting Hatch Driver Camera")
    
    # Initialize camera
    camera = CameraServer.getInstance() \
        .startAutomaticCapture(name="Hatch Driver Camera", path="/dev/video2")
    
    # Sets the resolution of the camera
    camera.setResolution (visionConstants.width, visionConstants.height)
    # Sets the config JSON to that defined in visionConstants
    camera.setConfigJson(visionConstants.cameraPropertiesJSON);
    
    # Return the created camera
    return camera

# Initializes and sets up the Ball Vision camera
def initializeBallVisionCap():
    
    # Print out statement for intializing the camera
    print("Starting Ball Vision Camera")
    
    # Initialize camera
    camera = CameraServer.getInstance() \
        .startAutomaticCapture(name="Ball Vision Camera", path="/dev/v4l/by-path/platform-3f980000.usb-usb-0:1.3:1.0-video-index0")
    
    # Sets the resolution of the camera
    camera.setResolution (visionConstants.width, visionConstants.height)
    # Sets the config JSON to that defined in visionConstants
    camera.setConfigJson(visionConstants.cameraPropertiesJSON);
    
    # Return the created camera
    return camera

# Init function for starting the cameras
def init():

    # Initialize and define the properties of the camera
    global hatchCam
    hatchCam = initializeHatchVisionCap()
    global ballCam
    ballCam = initializeBallVisionCap();
    initializeHatcherDriverCap();


# Returns an image sink for processing frames from the hatch vision camera
def getHatchVisionCameraSink():
    # Get a CvSink that will capture images from the camera for processing
    return CameraServer.getInstance().getVideo(camera=hatchCam);

# Returns an image sink for processing frames from the ball vision camera
def getBallVisionCameraSink():
    # Get a CvSink that will capture images from the camera for processing
    return CameraServer.getInstance().getVideo(camera=ballCam);

# Returns a stream for sending processed frames
def getVisionStream():
    # Setup a CvSource. This will send images back to the computer
    return CameraServer.getInstance().putVideo("Vision Output Camera Stream", visionConstants.width, visionConstants.height)
