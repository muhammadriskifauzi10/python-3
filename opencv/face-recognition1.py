import os
import cv2
import face_recognition
from PIL import Image

os.system('cls')

img = face_recognition.load_image_file('assets/images/img1.jpg')

img_local = face_recognition.face_locations(img)

for (t,r,b,l) in img_local:
    face_image = img[t:b, l:r]
    pil_image = Image.fromarray(face_image)
    pil_image.show()
