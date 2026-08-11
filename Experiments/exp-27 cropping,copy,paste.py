import cv2

img = cv2.imread('image.png')

# Crop region
crop = img[50:200, 50:200]



cv2.imshow("Crop & Paste", img)
cv2.waitKey(0)
cv2.destroyAllWindows()