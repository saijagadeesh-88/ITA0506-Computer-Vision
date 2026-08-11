import cv2

img = cv2.imread('image.png')

watermark = "MyName"

cv2.putText(img, watermark, (50, 50),
            cv2.FONT_HERSHEY_SIMPLEX, 1,
            (255, 255, 255), 2, cv2.LINE_AA)

cv2.imshow("Watermarked", img)
cv2.waitKey(0)
cv2.destroyAllWindows()