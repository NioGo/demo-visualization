import cv2
im = cv2.imread("test.jpg", 0)
ret, th = cv2.threshold(im, 180, 255, cv2.THRESH_BINARY)
cv2.imshow("demo", th)
cv2.waitKey(0)
cv2.imwrite("binary.jpg", th)