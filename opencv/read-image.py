import os
import cv2 as cv

os.system('cls')

img = cv.imread('assets/images/img1.jpg', cv.COLOR_BGR2GRAY)

img_r = cv.resize(img, (570, 720))

cv.imshow('Display', img_r)

cv.waitKey(0)