import cv2

# Open video
cap = cv2.VideoCapture("expi6.mp4")

if not cap.isOpened():
    print("Video not found")
    exit()

# Store all frames
frames = []

while True:

    ret, frame = cap.read()

    if not ret:
        break

    frames.append(frame)

cap.release()

# Play frames in reverse
for frame in reversed(frames):

    cv2.imshow("expi6", frame)

    # Press ESC to stop
    if cv2.waitKey(30) & 0xFF == 27:
        break

cv2.destroyAllWindows()