import cv2

# Read the main image
img = cv2.imread(".png")

# Read the watch template
template = cv2.imread("watch.png")

if img is None:
    print("Error: image.png not found")
    exit()

if template is None:
    print("Error: watch_template.png not found")
    exit()

# Convert images to grayscale
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray_template = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)

# Template matching
result = cv2.matchTemplate(
    gray_img,
    gray_template,
    cv2.TM_CCOEFF_NORMED
)

# Find best matching location
_, max_val, _, max_loc = cv2.minMaxLoc(result)

# Threshold
threshold = 0.6

if max_val >= threshold:

    h, w = gray_template.shape

    x, y = max_loc

    # Draw rectangle around watch
    cv2.rectangle(
        img,
        (x, y),
        (x + w, y + h),
        (0, 255, 0),
        2
    )

    cv2.putText(
        img,
        "WATCH",
        (x, y - 10),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.8,
        (0, 255, 0),
        2
    )

    print("Watch detected")
    print("Confidence:", max_val)

else:
    print("Watch not detected")

# Display result
cv2.imshow("Watch Recognition", img)

cv2.waitKey(0)
cv2.destroyAllWindows()