import cv2
import numpy as np

img = cv2.imread('image.png')

if img is None:
    print("Error: Image not found")
    exit()

h, w = img.shape[:2]

pts1 = np.float32([[0, 0],
                   [w-1, 0],
                   [w-1, h-1],
                   [0, h-1]])

pts2 = np.float32([[50, 50],
                   [w-100, 30],
                   [w-50, h-50],
                   [30, h-100]])

H = cv2.getPerspectiveTransform(pts1, pts2)

dlt = cv2.warpPerspective(img, H, (w, h))

cv2.imshow("Original", img)
cv2.imshow("DLT Result", dlt)
cv2.waitKey(0)
cv2.destroyAllWindows()