import cv2
import numpy as np

img = cv2.imread('image.png', 0)

# Sobel X and Y
sobelx = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=3)
sobely = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=3)

# Magnitude
gradient = cv2.magnitude(sobelx, sobely)
gradient = cv2.convertScaleAbs(gradient)

# Add to original for sharpening
sharpened = cv2.add(img, gradient)

cv2.imshow("Gradient Sharpening", sharpened)
cv2.waitKey(0)
cv2.destroyAllWindows()