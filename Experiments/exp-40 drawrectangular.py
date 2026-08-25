import cv2

# Read image
img = cv2.imread("cvexp.png")

if img is None:
    print("Image not found")
    exit()

# Select rectangular region
x = 100
y = 100
w = 200
h = 200

# Draw rectangle
cv2.rectangle(
    img,
    (x, y),
    (x + w, y + h),
    (0, 255, 0),
    2
)

# Extract object
object_img = img[y:y+h, x:x+w]

# Display
cv2.imshow("Original with Rectangle", img)
cv2.imshow("Extracted Object", object_img)

cv2.waitKey(0)
cv2.destroyAllWindows()