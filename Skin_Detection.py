import numpy as np
import cv2

# Read and process the image
img = cv2.imread('faces.jpeg', 1)
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

h = hsv[:, :, 0]
s = hsv[:, :, 1]
v = hsv[:, :, 2]

# Concatenate the HSV channels
hsv_split = np.concatenate((h, s, v), axis=1)

# Resize the concatenated image
resize_scale = 0.25  # Adjust this scale factor as needed
new_size = (int(hsv_split.shape[1] * resize_scale), int(hsv_split.shape[0] * resize_scale))
resized_hsv_split = cv2.resize(hsv_split, new_size)

# Display the resized image
cv2.imshow("Split HSV", resized_hsv_split)

cv2.waitKey(0)
cv2.destroyAllWindows()
