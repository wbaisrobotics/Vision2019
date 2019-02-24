# Vision2019

Platform developed in python and intended to use with a Raspberry Pi Model 3B or better. Utilizes opencv, cscore, and network tables to process images from connecting camera(s) through multiple filters and find targets for the FIRST Robotics Competition (FRC). Currently optimized for detecting the refelctive-tape targets in FIRST Deep Space.

Measures the differences in x & y (relative to the center of the screen) in addition to other variables and then immediately flushes the values through the network tables — intended to be received by the roborio and subsequently followed. 

File summaries:
run - the main class that starts the program and contains the main loop
cameraManager - manages the connections to the cameras and the streams to/from the dashboard through CameraServer
contourProcessor - processes the images from the cameras and locates various contours/targets
visionConstants  - the constants (static and dynamic) for vision processing
networkConstants - contains the constants for the network tables (such as keys)
networkTables - manages the network table communication to/from the roborio server

Property of Falcons Robotics (FRC #4338). Programmed by Orian Leitersdorf.
