from Facedetection import Face_detection as fd
from Facerecognition import Face_recognition as fr
def annotate(image):
    image=fd.detectFace(image)
    image=fr.recognizeFace(image)
    
    return image