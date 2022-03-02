import os
import cv2 as cv

os.system('cls')

img = cv.imread('assets/images/img1.jpg')

img_r1 = cv.resize(img, (500, 700))

# Blur
img_blur = cv.GaussianBlur(img_r1, (7,7), cv.BORDER_DEFAULT)

# Canny
img_canny = cv.Canny(img_blur, 125, 175)

# Dilate
img_dilate = cv.dilate(img_canny, (7,7), iterations=2)

contours, h = cv.findContours(img_dilate, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)

cv.imshow('Display', img_dilate)

print("Amount contour :", len(contours))

cv.waitKey(0)