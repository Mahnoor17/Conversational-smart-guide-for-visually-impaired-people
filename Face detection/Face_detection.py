import numpy as np
from pylab import *
import cv2
def detectFace(image):
    face_cascade = cv2.CascadeClassifier('dataset/haarcascade_frontalface_default.xml')
    path=cv2.imread(image)
    gray = cv2.cvtColor(path, cv2.COLOR_BGR2GRAY)
    # Detect faces
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)
    # Draw rectangle around the faces
    for (x, y, w, h) in faces:
        cv2.rectangle(path, (x, y), (x+w, y+h), (255, 0, 0), 2)
    # Display the output
    cv2.imshow('image', path)
    cv2.waitKey() #as no digit is written in wait key,so the image screen will close when we press any key..
    cv2.destroyAllWindows()
    return gray
output=detectFace('images/test.jpg')
    
