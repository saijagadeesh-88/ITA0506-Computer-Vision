import cv2

img = cv2.imread('image.png')

if img is None:
    print("Error: Image not found")
    exit()

# Blur image
blur = cv2.GaussianBlur(img, (5,5), 0)

A = 1.5   # High-boost factor (>=1)

# High-boost sharpening
high_boost = cv2.addWeighted(img, A, blur, -(A-1), 0)

cv2.imshow("High Boost", high_boost)
cv2.waitKey(0)
cv2.destroyAllWindows()