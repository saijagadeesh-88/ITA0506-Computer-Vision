import cv2

# Open video
cap = cv2.VideoCapture("traffic.mp4")

if not cap.isOpened():
    print("Video not found")
    exit()

# Background subtractor
background = cv2.createBackgroundSubtractorMOG2()

while True:

    ret, frame = cap.read()

    if not ret:
        break

    # Create foreground mask
    mask = background.apply(frame)

    # Remove noise
    mask = cv2.morphologyEx(
        mask,
        cv2.MORPH_OPEN,
        cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
    )

    # Find contours
    contours, _ = cv2.findContours(
        mask,
        cv2.RETR_EXTERNAL,
        cv2.CHAIN_APPROX_SIMPLE
    )

    for contour in contours:

        area = cv2.contourArea(contour)

        if area > 500:

            x, y, w, h = cv2.boundingRect(contour)

            cv2.rectangle(
                frame,
                (x, y),
                (x + w, y + h),
                (0, 255, 0),
                2
            )

            cv2.putText(
                frame,
                "Vehicle",
                (x, y - 10),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.6,
                (0, 255, 0),
                2
            )

    cv2.imshow("Vehicle Detection", frame)

    # Press ESC to exit
    if cv2.waitKey(30) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()