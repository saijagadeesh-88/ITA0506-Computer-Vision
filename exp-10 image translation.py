import cv2
import numpy as np
img = cv2.imread('image.png')
tx, ty = 100, 50   
M = np.float32([[1, 0, tx], [0, 1, ty]])
shifted = cv2.warpAffine(img, M, (img.shape[1], img.shape[0]))
cv2.imshow("Translated", shifted)
cv2.waitKey(0)
cv2.destroyAllWindows()

