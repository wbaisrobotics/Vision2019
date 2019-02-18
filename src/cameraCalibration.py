
# Import numpy for matrix managment
import numpy as np

# Import opencv for image processing
import cv2 as cv

# Import glob for accesing and searching for files
import glob

# Calibrates the camera using chess board photos
# Chess board photos stored at "/home/pi/images/" as .png files
def calibrate():

    # The termination criteria for cv.cornerSubPix
    criteria = (cv.TERM_CRITERIA_EPS + cv.TERM_CRITERIA_MAX_ITER, 30, 0.001)
    # Prepare the locations of the points
    objp = np.zeros((6 * 5, 3), np.float32)
    objp[:, :2] = np.mgrid[0:5, 0:6].T.reshape(-1, 2)
    # Calibrate to the actual physical size of the board
    objp *= 40;
    
    # Arrays to store object points and image points from all the images.
    objpoints = [] # 3d point in real world space
    imgpoints = [] # 2d points in image plane.
    
    # Access all of the images in the "images" folder
    images = glob.glob ("/home/pi/images/*.png")
    # Print out all of the files that will be analyzed
    print ("Found the following files: ");
    print (images);
    
    # Initialize the matricies for the total sums (to be used to calculate average)
    totalDist = np.zeros ((1, 5), np.float32);
    totalMat = np.zeros ((3, 3), np.float32);
    
    # Start counter (to be used for average)
    n = 0;
    
    # Iterate through each file name in the folder
    for fname in images:
        
        # Increase the counter
        n = n + 1;
        
        # Read the image at the file name
        img = cv.imread(fname)
        # Log the current file name
        print (fname);
        # Convert to grayscale image
        gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
        # Find the chess board corners
        ret, corners = cv.findChessboardCorners(gray, (6,5), None)
        # If found, add object points, image points (after refining them)
        if ret == True:
            # Save the objpoints from real-world coordinates
            objpoints.append(objp)
            # Calculate the corners of the board
            corners2 = cv.cornerSubPix(gray,corners, (11,11), (-1,-1), criteria)
            # Save the corners
            imgpoints.append(corners)
            # Draw and display the corners
            cv.drawChessboardCorners(img, (6,5), corners2, ret)
            # Save the image with the drawn corners
            cv.imwrite("%s Output.png" % fname[:-4], img);
            # Calculate the constants given the found coordinates
            ret, mtx, dist, rvecs, tvecs = cv.calibrateCamera(objpoints, imgpoints, gray.shape[::-1], None, None)
            # Add to total distortion matrix
            totalDist += dist;
            # Add to total matrix mat
            totalMat += mtx;
            # Print out what was found
            print (fname)
            print (dist);
            print (mtx);

    # Print out the averages
    print ("Averaged Results: ");
    print ("Avg Distortion: ");
    print(totalDist / n);
    print ("Avg Matrix: ");
    print(totalMat / n);
