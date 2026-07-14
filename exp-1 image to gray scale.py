import cv2 
image = cv2.imread("image.png")  
if image is None:
    print("Error: Could not load image. Check the file path.")
else:
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) 
    cv2.imshow("Original Image", image) 
    cv2.imshow("Grayscale Image", gray_image) 
    cv2.waitKey(0) 
    cv2.destroyAllWindows() 