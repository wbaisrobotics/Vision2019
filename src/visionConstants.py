
#### File defining the constants for vision processing

# Whether or not vision should run
run = True;

# Whether the ball cam is the cam being processed
reverse = False;

### Camera Properties

## Define properties

# The contrast of the image
contrast = 100;
# The saturation of the image
saturation = 100;
# Manual Exposure (1) or Auto Exposure (0)
auto_exposure = 1;
# The exposure time (in ms)
exposure_time_absolute = 0;
# The brightness of the image
brightness = 0;
# The width of the image
width = 176;
# The height of the image
height = 144;

## Define the JSON using the constants
cameraPropertiesJSON = '{"properties": [{"name": "contrast","value": %d}, {"name": "saturation","value": %d}, {"name":"exposure_auto","value":%d}, {"name":"exposure_absolute","value":%d}, {"name":"brightness","value":%d}]}' % (contrast, saturation, auto_exposure, exposure_time_absolute, brightness);


### Vision Properties

## HSV Filtering

# The default hue low value (0 to 360) - can be overriden during run time
hueLow = 0;
# The default hue high value (0 to 360) - can be overriden during run time
hueHigh = 50;

# The default sat low value (0 to 255) - can be overriden during run time
satLow = 150;
# The default sat high value (0 to 255) - can be overriden during run time
satHigh = 255;

# The default val low value (0 to 255) - can be overriden during run time
valLow = 0;
# The default val high value (0 to 255) - can be overriden during run time
valHigh = 50;

## Contour selections

# Minimum area
minArea = 30

# Minimum rect fill
minRectFill = 0.5

# Target angle between two rects (from manual) - in degrees
targetAngle = 30
# Acceptable target angle error (in either direction)
targetAngleError = 15

# Target ratio for the target (total width / rect height average)
targetRatio = 2.7854545455;
# Acceptable target ratio error (in either direction)
targetRatioError = 1.0
