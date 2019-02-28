
# Import network tables (FRC Library) for communicating with other nodes on the network
from networktables import NetworkTablesInstance

# For updating the HSV ranges
import visionConstants

# For the network table settings
import networkConstants

# Initializes the network table connection
def init ():
    # Log the beginning of the network table client
    print("Setting up NetworkTables client for team 4338")
    # Get an instance of the "portal"
    ntinst = NetworkTablesInstance.getDefault()
    # Attempt to start a connection at our team number
    ntinst.startClientTeam(4338)
    # Define the table as a global variable
    global table
    # Attempt to get the SmartDashboard table and store it
    table = ntinst.getTable (networkConstants.tableName)

    # Write the current HSV settings
    # Write hue low
    table.putNumber (networkConstants.hueLowKey, visionConstants.hueLow)
    # Write hue high
    table.putNumber (networkConstants.hueHighKey, visionConstants.hueHigh)
    # Write sat low
    table.putNumber (networkConstants.satLowKey, visionConstants.satLow)
    # Write sat high
    table.putNumber (networkConstants.satHighKey, visionConstants.satHigh)
    # Write val low
    table.putNumber (networkConstants.valLowKey, visionConstants.valLow)
    # Write val high
    table.putNumber (networkConstants.valHighKey, visionConstants.valHigh)

    # Write default run to true
    table.putBoolean (networkConstants.runKey, True)
    
    # Write default reverse to false
    table.putBoolean (networkConstants.reverseKey, False);

    # Call for an update
    update();

# Updates the HSV range stored in visionConstants to values from the table
def updateHSVRange ():
    
    # Retrieve the hueLow value (with default value being the current value)
    visionConstants.hueLow = table.getNumber (networkConstants.hueLowKey, visionConstants.hueLow)
    # Retrieve the hueHigh value (with default value being the current value)
    visionConstants.hueHigh = table.getNumber (networkConstants.hueHighKey, visionConstants.hueHigh)
    
    # Retrieve the satLow value (with default value being the current value)
    visionConstants.satLow = table.getNumber (networkConstants.satLowKey, visionConstants.satLow)
    # Retrieve the satHigh value (with default value being the current value)
    visionConstants.satHigh = table.getNumber (networkConstants.satHighKey, visionConstants.satHigh)
    
    # Retrieve the valLow value (with default value being the current value)
    visionConstants.valLow = table.getNumber (networkConstants.valLowKey, visionConstants.valLow)
    # Retrieve the valHigh value (with default value being the current value)
    visionConstants.valHigh = table.getNumber (networkConstants.valHighKey, visionConstants.valHigh)

# Runs for each frame to update settings before next frame
def update ():
    
    # Update the HSV range
    updateHSVRange()
    
    # Update the run boolean
    visionConstants.run = table.getBoolean (networkConstants.runKey, True);

    # Update the reverse boolean
    visionConstants.reverse = table.getBoolean (networkConstants.reverseKey, True);

# Sends the target data for xDiff, yDiff, heighRatio, and ttsr
def sendTargetData (xDiff, yDiff, heightRatio, ttsr):

    # Send the x difference
    table.putNumber (networkConstants.xDiffKey, xDiff);

    # Send the y difference
    table.putNumber (networkConstants.yDiffKey, yDiff);

    # Send the height ratio
    table.putNumber (networkConstants.heightRatioKey, heightRatio);
    
    # Send the ttsr
    table.putNumber (networkConstants.ttsrKey, ttsr);

    # Flush the table in order to immediately send the values
    NetworkTablesInstance.getDefault().flush();


