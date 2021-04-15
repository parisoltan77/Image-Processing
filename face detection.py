#Programmed by Soltanzadeh & Tabatabaee

import cv2

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')
smile_cascade = cv2.CascadeClassifier('haarcascade_smile.xml')

img = cv2.imread('pic1.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(gray, 1.3, 5)
for (x,y,w,h) in faces:
    img = cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
    roi_gray = gray[y:y+h, x:x+w]
    roi_color = img[y:y+h, x:x+w]
    #eyes
    eyes = eye_cascade.detectMultiScale(roi_gray,1.2,18)
    for (ex,ey,ew,eh) in eyes:
        cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
    #smile :)
    smile = smile_cascade.detectMultiScale(roi_gray, 1.7, 20)
    for (x_smile, y_smile, w_smile, h_smile) in smile:
        cv2.rectangle(roi_color,(x_smile, y_smile),(x_smile+w_smile, y_smile+h_smile), (0, 0, 255), 2)

cv2.imshow('img',img)
cv2.waitKey(0)
cv2.destroyAllWindows()