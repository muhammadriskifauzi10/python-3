import os
from pickle import FALSE
import cv2 as cv

os.system('cls')

valueFF = 1.1
valueFFF = -1

mask_on = False

face_detect_face = cv.CascadeClassifier('assets/xml/face-default.xml')
face_detect_nose = cv.CascadeClassifier('assets/xml/nose.xml')

cap = cv.VideoCapture(0)

while True:
    ret, frame = cap.read()

    face_finish_face = face_detect_face.detectMultiScale(frame, valueFF, valueFFF)
    
    for (x1,y1,w1,h1) in face_finish_face:

        if mask_on:
            cv.rectangle(frame, (x1,y1), (w1+x1, h1+y1), (0,0,255), thickness=3)
        else:
            cv.putText(frame, 'Pakai masker', (10, 450), cv.FONT_HERSHEY_SIMPLEX, 1.1, (0,255,0), thickness=3)

    face_finish_nose = face_detect_nose.detectMultiScale(frame, 1.1, 20)
    
    for (x2,y2,w2,h2) in face_finish_nose:
        cv.rectangle(frame, (x2,y2), (w2+x2, h2+y2), (0,0,255), thickness=3)
        cv.putText(frame, 'Tidak pakai masker', (10, 450), cv.FONT_HERSHEY_SIMPLEX, 1.1, (0,0,255), thickness=3)

    if len(face_finish_nose) > 0:
        mask_on = True
        valueFFF = 2
        valueFF - 1.2
    else:
        mask_on = False
        valueFFF = -1
        valueFF - 1.1
    
    cv.imshow('Display', frame)
        
    if cv.waitKey(1) == ord('q'):
        break


cap.release()
cv.destroyAllWindows()