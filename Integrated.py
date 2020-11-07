from Facedetection import Face_detection as fd
from Facerecognition import Face_recognition as fr
from Objectdetection import Object_detection as od
from SceneRecognition import Scene_recognition as sr

def annotate(image):
    #image = fd.detectFace(image)
    image,name = fr.recognizeFace(image)
    image = od.detectObject(image)
    image,predictions = sr.recognizeScene(image)
    
    return image