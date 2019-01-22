
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
exposure_time_absolute = 214;
# The brightness of the image
brightness = 35;
# The width of the image
width = 320;
# The height of the image
height = 240;

## Define the JSON using the constants
cameraPropertiesJSON = '{"properties": [{"name": "contrast","value": %d}, {"name": "saturation","value": %d}, {"name":"auto_exposure","value":%d}, {"name":"exposure_time_absolute","value":%d}, {"name":"brightness","value":%d}]}' % (contrast, saturation, auto_exposure, exposure_time_absolute, brightness);


### Vision Properties

## HSV Filtering

# The default hue low value (0 to 180) - can be overriden during run time
hueLow = 32;
# The default hue high value (0 to 180) - can be overriden during run time
hueHigh = 87;

# The default sat low value (0 to 255) - can be overriden during run time
satLow = 0;
# The default sat high value (0 to 255) - can be overriden during run time
satHigh = 62;

# The default val low value (0 to 255) - can be overriden during run time
valLow = 242;
# The default val high value (0 to 255) - can be overriden during run time
valHigh = 255;

## Contour selection

# Minimum area
minArea = 400

# Minimum rect fill
minRectFill = 0.7

# Target angle between two rects (from manual) - in degrees
targetAngle = 14.5
