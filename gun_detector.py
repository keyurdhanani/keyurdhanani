import numpy as np
import cv2
import imutils
import os
print(os.getcwd())

# Load the gun cascade file
gun_cascade = cv2.CascadeClassifier('D:\Python Programming\Python Projects\Geeks Projects Python\Gun Detector\cascade.xml')

# Initialize the camera
camera = cv2.VideoCapture(0)
first_frame = None
gun_exist = False

while True:
    # Read the frame from the camera
    ret, frame = camera.read()
    if not ret:
        print("Failed to grab frame. Exiting...")
        break

    frame = imutils.resize(frame, width=500)
    
    # Convert the frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # Detect guns in the frame
    guns = gun_cascade.detectMultiScale(gray, 1.3, 5, minSize=(100, 100))
    
    if len(guns) > 0:
        gun_exist = True
        for (x, y, w, h) in guns:
            # Draw rectangle around the detected gun
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
    else:
        gun_exist = False
    
    # Initialize the first frame
    if first_frame is None:
        first_frame = gray
        continue
    
    # Display the frame
    cv2.imshow("Security Feed", frame)
    
    # Break the loop if 'q' is pressed or the window is closed
    key = cv2.waitKey(1) & 0xFF
    if key == ord('q') or cv2.getWindowProperty("Security Feed", cv2.WND_PROP_VISIBLE) < 1:
        break
    
    # Print detection status
    if gun_exist:
        print("Guns detected")
    else:
        print("No guns detected")

# Release the camera and destroy all windows
camera.release()
cv2.destroyAllWindows()
