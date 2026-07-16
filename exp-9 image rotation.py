import cv2

img = cv2.imread('image.png')
(h, w) = img.shape[:2]
center = (w // 2, h // 2)

M1 = cv2.getRotationMatrix2D(center, -45, 1.0)
rot_cw = cv2.warpAffine(img, M1, (w, h))

M2 = cv2.getRotationMatrix2D(center, 45, 1.0)
rot_ccw = cv2.warpAffine(img, M2, (w, h))

cv2.imshow("CW", rot_cw)
cv2.imshow("CCW", rot_ccw)
cv2.waitKey(0)
cv2.destroyAllWindows()