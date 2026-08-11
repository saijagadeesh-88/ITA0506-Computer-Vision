import cv2
import numpy as np

img = cv2.imread('image.png')

if img is None:
    print("Error: Image not found")
    exit()

# Positive center Laplacian kernel
kernel = np.array([[0, -1, 0],
                   [-1, 5, -1],
                   [0, -1, 0]])

sharpened = cv2.filter2D(img, -1, kernel)

cv2.imshow("Original", img)
cv2.imshow("Sharpened (Positive Center)", sharpened)
cv2.waitKey(0)
cv2.destroyAllWindows()