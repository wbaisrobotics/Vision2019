
#### File defining the constants for vision processing

import numpy as np

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
width = 640;
# The height of the image
height = 480;

## Define the JSON using the constants
cameraPropertiesJSON = '{"properties": [{"name": "contrast","value": %d}, {"name": "saturation","value": %d}, {"name":"auto_exposure","value":%d}, {"name":"exposure_time_absolute","value":%d}, {"name":"brightness","value":%d}]}' % (contrast, saturation, auto_exposure, exposure_time_absolute, brightness);


### Vision Properties

## HSV Filtering

# The default hue low value (0 to 360) - can be overriden during run time
hueLow = 100;
# The default hue high value (0 to 360) - can be overriden during run time
hueHigh = 255;

# The default sat low value (0 to 255) - can be overriden during run time
satLow = 0;
# The default sat high value (0 to 255) - can be overriden during run time
satHigh = 100;

# The default val low value (0 to 255) - can be overriden during run time
valLow = 0;
# The default val high value (0 to 255) - can be overriden during run time
valHigh = 100;

## Contour selection

# Minimum area
minArea = 100

# Minimum rect fill
minRectFill = 0.7

# Target angle between two rects (from manual) - in degrees
targetAngle = 30


## Camera constants
#dist_coeffs = np.matrix([-0.02268737165058874, 1.390462222445477, 0.004819439816432395, -0.001004285293114526, -7.728654197858665]);
#mat = np.matrix([[1272.76594852567, 0, 644.2288328934579],
#                 [0, 1282.754546606928, 479.4776196896662],
#                 [0, 0, 1]]);
#
## FIRST Deep Space constants
#model_points = np.matrix([
#
# # Left target
# [-5.37709, -3.199812, 0.0], # Bottom right
# [-6.69996, -2.699812, 0.0], # Bottom left
# [-5.32288, 2.625, 0.0], # Top left
# [-4, 2.125, 0.0], # Top right
#
# # Right target
# [5.37709, -3.199812, 0.0], # Bottom left
# [4, 2.125, 0.0], # Top left
# [5.32288, 2.625, 0.0], # Top right
# [6.69996, -2.699812, 0.0] # Bottom right
#
#])
