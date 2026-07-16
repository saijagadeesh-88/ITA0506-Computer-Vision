import cv2
import numpy as np
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    pts1 = np.float32([[50,50],[300,50],[50,300],[300,300]])
    pts2 = np.float32([[0,0],[300,0],[0,300],[300,300]])

    M = cv2.getPerspectiveTransform(pts1, pts2)
    warped = cv2.warpPerspective(frame, M, (300,300))

    cv2.imshow("Video Perspective", warped)

    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()