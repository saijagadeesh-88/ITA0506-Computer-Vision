import cv2
import numpy as np
img = cv2.imread('image.png')

pts_src = np.array([[50,50],[200,50],[200,200],[50,200]])
pts_dst = np.array([[10,100],[200,50],[220,250],[100,300]])

H, status = cv2.findHomography(pts_src, pts_dst)
homography = cv2.warpPerspective(img, H, (300,300))

cv2.imshow("Homography", homography)
cv2.waitKey(0)
cv2.destroyAllWindows()