import cv2
img = cv2.imread('image.png', 0)

sobely = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=5)

cv2.imshow("Sobel Y", sobely)
cv2.waitKey(0)
cv2.destroyAllWindows()