import numpy as np
import cv2
import pytesseract


img = cv2.imread("book_pg.jpg")
# img =cv2.resize(img, None, fx=0.2, fy=0.2)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

adaptive_threshold = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 85, 9)
config = "--psm 3"
text = pytesseract.image_to_string(adaptive_threshold, config=config)
print(text)

cv2.imshow("adapt", adaptive_threshold)
cv2.waitKey(0)