import cv2

img = cv2.imread('image.png')

if img is None:
    print("Error: Image not found")
    exit()

# Step 1: Blur image
blur = cv2.GaussianBlur(img, (5,5), 0)

# Step 2: Create mask
mask = cv2.subtract(img, blur)

# Step 3: Add mask to original
sharpened = cv2.add(img, mask)

cv2.imshow("Original", img)
cv2.imshow("Unsharp Mask", sharpened)
cv2.waitKey(0)
cv2.destroyAllWindows()