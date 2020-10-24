from Facedetection import Face_detection as fd
from Facerecognition import Face_recognition as fr
from Objectdetection import Object_detection as od

def annotate(image):
    image = fd.detectFace(image)
    image = fr.recognizeFace(image)
    image = od.detectObject(image)
    
    return image