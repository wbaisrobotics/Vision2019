
## File managing the cameras associated with the program

# Import the constants for vision processing
import visionConstants

# Import cscore (FRC Library) for connecting more efficently to the streaming servers and cameras
from cscore import CameraServer, VideoSource, UsbCamera

# Initializes and sets up the Hatch Vision camera
def initializeHatchVisionCap():
    
    # Print out statement for intializing the camera
    print("Starting Hatch Vision Camera")
    
    # Get the camera server instance
    inst = CameraServer.getInstance()
    # Initialize the UsbCamera at the given port with the name from the webdashboard
    camera = UsbCamera("Hatch Vision", "/dev/v4l/by-path/platform-3f980000.usb-usb-0:1.4:1.0-video-index0")
    # Initialize the server for sending the images frmo the UsbCamera
    server = inst.startAutomaticCapture(camera=camera, return_server=True)
    
    # Set the FPS of the camera
    camera.setFPS (30);
    # Set the connection strategy for the camera to maintain open
    camera.setConnectionStrategy(VideoSource.ConnectionStrategy.kKeepOpen)

    # Set the resolution of the camera
    camera.setResolution (visionConstants.width, visionConstants.height)
    # Set the config JSON to that defined in visionConstants
    camera.setConfigJson(visionConstants.cameraPropertiesJSON);
    
    ## For stream compression
    # Define a config for the stream (for compression)
    streamConfig = '{"properties": [{"name": "compression","value": 50}]}';
    # Set the config to the stream
    server.setConfigJson(streamConfig)
    
    return camera

# Initializes and sets up the Hatch Driver camera
def initializeHatcherDriverCap():
    
    # Print out statement for intializing the camera
    print("Starting Hatch Driver Camera")

    # Get the camera server instance
    inst = CameraServer.getInstance()
    # Initialize the UsbCamera at the given port with the name from the webdashboard
    camera = UsbCamera("Hatch Driver", "/dev/v4l/by-path/platform-3f980000.usb-usb-0:1.3:1.0-video-index0")
    # Initialize the server for sending the images frmo the UsbCamera
    server = inst.startAutomaticCapture(camera=camera, return_server=True)
    
    # Set the resolution of the camera
    camera.setResolution (160, 120)
    # Set the brightness of the camera
    camera.setBrightness (30);
    # Set the FPS of the camera
    camera.setFPS (10);
    # Set the camera to auto exposure
    camera.setExposureAuto ();
    
    # Set the connection strategy for the camera to maintain open
    camera.setConnectionStrategy(VideoSource.ConnectionStrategy.kKeepOpen)
    
    ## For stream compression
    # Define a config for the stream (for compression)
    streamConfig = '{"properties": [{"name": "compression","value": 50}]}';
    # Set the config to the stream
    server.setConfigJson(streamConfig)
    
    return camera

# Initializes and sets up the Ball Vision camera
def initializeBallVisionCap():
    
    # Print out statement for intializing the camera
    print("Starting Ball Vision Camera")
    
    # Get the camera server instance
    inst = CameraServer.getInstance()
    # Initialize the UsbCamera at the given port with the name from the webdashboard
    camera = UsbCamera("Ball", "/dev/v4l/by-path/platform-3f980000.usb-usb-0:1.5:1.0-video-index0")
    # Initialize the server for sending the images frmo the UsbCamera
    server = inst.startAutomaticCapture(camera=camera, return_server=True)
    
    # Set the resolution of the camera
    camera.setResolution (160, 120)
    # Set the brightness of the camera
    camera.setBrightness (30);
    # Set the FPS of the camera
    camera.setFPS (10);
    # Set the camera to auto exposure
    camera.setExposureAuto ();
    
    # Set the connection strategy for the camera to maintain open
    camera.setConnectionStrategy(VideoSource.ConnectionStrategy.kKeepOpen)
    
    ## For stream compression
    # Define a config for the stream (for compression)
    streamConfig = '{"properties": [{"name": "compression","value": 50}]}';
    # Set the config to the stream
    server.setConfigJson(streamConfig)
    
    return camera

# Init function for starting the cameras
def init():

    # Initialize and define the properties of the camera
    global hatchCam
    hatchCam = initializeHatchVisionCap();
    global ballCam
    ballCam = initializeBallVisionCap();
    initializeHatcherDriverCap();

def lowBrtMode():

    hatchCam.setExposureManual (0);

def highBrtMode():

    hatchCam.setExposureAuto ();


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
