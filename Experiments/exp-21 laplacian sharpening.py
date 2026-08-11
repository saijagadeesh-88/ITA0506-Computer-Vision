import cv2
import numpy as np

img = cv2.imread('image.png')

if img is None:
    print("Error: Image not found")
    exit()

# Define Laplacian kernel (8-neighbors)
kernel = np.array([[1, 1, 1],
                   [1, -8, 1],
                   [1, 1, 1]])

# Apply filter
laplacian = cv2.filter2D(img, -1, kernel)

# Sharpening: original - laplacian
sharpened = cv2.subtract(img, laplacian)

cv2.imshow("Original", img)
cv2.imshow("Sharpened (Diagonal Laplacian)", sharpened)
cv2.waitKey(0)
cv2.destroyAllWindows()