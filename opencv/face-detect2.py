import os
import cv2 as cv

os.system('cls')

img = cv.imread('assets/images/img1.jpg')

img_r = cv.resize(img, (500, 700))

detect_face = cv.CascadeClassifier('assets/xml/nose.xml')

detect_finish = detect_face.detectMultiScale(img_r, scaleFactor=1.2, minNeighbors=12)

print(len(detect_finish))

cv.waitKey(0)