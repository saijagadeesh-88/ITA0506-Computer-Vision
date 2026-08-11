import cv2
import numpy as np

img = cv2.imread('image.png', 0)

kernel = np.array([[0, -1, 0],
                   [-1, 4, -1],
                   [0, -1, 0]])

boundary = cv2.filter2D(img, -1, kernel)

cv2.imshow("Boundary", boundary)
cv2.waitKey(0)
cv2.destroyAllWindows()