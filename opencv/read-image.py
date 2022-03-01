import cv2 as cv

img = cv.imread('assets/images/img1.jpg')

cv.imshow('Display', img)

cv.waitKey(0)