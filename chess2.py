import cv2
import numpy as np

# Set up the camera
cap = cv2.VideoCapture(0)

# Define the chessboard dimensions
rows = 8
cols = 8

# Define the size of each square in pixels
square_size = 50

while True:
    # Read a frame from the camera
    ret, frame = cap.read()
    
    # Convert the frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # Find the corners of the chessboard
    ret, corners = cv2.findChessboardCorners(gray, (rows, cols), None)
    
    # If the corners are found, draw the lines
    if ret == True:
        corners = corners.reshape(-1, 2)
        
        # Create a blank image to draw the lines on
        img_lines = np.zeros_like(frame)
        
        # Draw the horizontal lines
        for i in range(1, rows):
            cv2.line(img_lines, tuple(corners[i*cols]), tuple(corners[i*cols + cols - 1]), (255, 0, 0), 2)
        
        # Draw the vertical lines
        for i in range(cols):
            cv2.line(img_lines, tuple(corners[i]), tuple(corners[(rows-1)*cols + i]), (255, 0, 0), 2)
        
        # Draw the lines on the original frame
        frame = cv2.addWeighted(frame, 0.5, img_lines, 0.5, 0)
    
    # Show the frame
    cv2.imshow('frame', frame)
    
    # Wait for a key press
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the camera and close all windows
cap.release()
cv2.destroyAllWindows()
