
#### File defining the constants for vision processing

### Camera Properties
## Define properties
# The contrast of the image
contrast = 100;
# The saturation of the image
saturation = 0;
# Manual Exposure (1) or Auto Exposure (0)
auto_exposure = 1;
# The exposure time (in ms)
exposure_time_absolute = 1;
# The brightness of the image
brightness = 50;
# The width of the image
width = 640;
# The height of the image
height = 480;

## Define the JSON using the constants
cameraPropertiesJSON = '{"properties": [{"name": "contrast","value": %d}, {"name": "saturation","value": %d}, {"name":"auto_exposure","value":%d}, {"name":"exposure_time_absolute","value":%d}, {"name":"brightness","value":%d}]}' % (contrast, saturation, auto_exposure, exposure_time_absolute, brightness);


### Vision Properties

