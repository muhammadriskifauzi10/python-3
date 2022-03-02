import os
import cv2 as cv
from cv2 import COLOR_BGR2GRAY

os.system('cls')

face_xml = cv.CascadeClassifier('assets/xml/face-default.xml')

img = cv.imread('assets/images/img1.jpg')

img_r1 = cv.resize(img, (500, 700))

c_c = cv.cvtColor(img_r1, COLOR_BGR2GRAY)

face_detect = face_xml.detectMultiScale(c_c, scaleFactor=1.1, minNeighbors=2)

for (x,y,w,h) in face_detect:
    show = cv.rectangle(c_c, (x,y), (w+x, h+y), 255, thickness=3)
    cv.imshow('Display', show)

print(face_detect)

cv.waitKey(0)