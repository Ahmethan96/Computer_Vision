import numpy as np
import cv2

# Read the image (in BGR format)
img = cv2.imread('detect_blob.png')

# Convert to grayscale (use cv2.COLOR_BGR2GRAY)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Apply adaptive thresholding
threshold = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)

# Display the thresholded image
cv2.imshow("Binary", threshold)

# Find contours (adjusted for OpenCV version 4.x)
contours, hierarchy = cv2.findContours(threshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# Prepare a copy of the original image to draw contours
img2 = img.copy()

# Parameters for drawing contours
index = -1
thickness = 4
color = (255, 0, 255)  # BGR color (magenta)

# Draw contours and their centers
for c in contours:
    cv2.drawContours(img2, [c], index, color, thickness)
    area = cv2.contourArea(c)
    perimeter = cv2.arcLength(c, True)

    M = cv2.moments(c)
    if M['m00'] != 0:  # Avoid division by zero
        cx = int(M['m10'] / M['m00'])
        cy = int(M['m01'] / M['m00'])
        cv2.circle(img2, (cx, cy), 4, (0, 0, 255), -1)

    print("Area: {}, Perimeter: {}".format(area, perimeter))

# Display the image with contours and centers
cv2.imshow("Contours", img2)

# Wait and then close the windows
cv2.waitKey(0)
cv2.destroyAllWindows()
