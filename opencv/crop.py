import imghdr
import os
import cv2 as cv

os.system('cls')

img = cv.imread('assets/images/img1.jpg')

img_r = cv.resize(img, (360, 500))

img_p = cv.rectangle(img_r, (100, 120), (275, 300), (0,255,0), thickness=3)

img_c = img_p[50:380, 80:300]

cv.imshow('Display2', img_c)

cv.waitKey()
cv.destroyAllWindows()