
#### File defining the constants for vision processing

# Whether or not vision should run
run = True;

### Camera Properties

## Define properties

# The contrast of the image
contrast = 100;
# The saturation of the image
saturation = 100;
# Manual Exposure (1) or Auto Exposure (0)
auto_exposure = 0;
# The exposure time (in ms)
exposure_time_absolute = 100;
# The brightness of the image
brightness = 0;
# The width of the image
width = 320;
# The height of the image
height = 240;

## Define the JSON using the constants
cameraPropertiesJSON = '{"properties": [{"name": "contrast","value": %d}, {"name": "saturation","value": %d}, {"name":"auto_exposure","value":%d}, {"name":"exposure_time_absolute","value":%d}, {"name":"brightness","value":%d}]}' % (contrast, saturation, auto_exposure, exposure_time_absolute, brightness);


### Vision Properties

## HSV Filtering

# The default hue low value (0 to 360) - can be overriden during run time
hueLow = 100;
# The default hue high value (0 to 360) - can be overriden during run time
hueHigh = 255;

# The default sat low value (0 to 255) - can be overriden during run time
satLow = 100;
# The default sat high value (0 to 255) - can be overriden during run time
satHigh = 255;

# The default val low value (0 to 255) - can be overriden during run time
valLow = 0;
# The default val high value (0 to 255) - can be overriden during run time
valHigh = 100;

## Contour selection

# Minimum area
minArea = 100

# Minimum rect fill
minRectFill = 0.6

# Target angle between two rects (from manual) - in degrees
targetAngle = 30
