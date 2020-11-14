from Facedetection import Face_detection as fd
from Facerecognition import Face_recognition as fr
from Objectdetection import Object_detection as od
from SceneRecognition import Scene_recognition as sr
from FacialExpressionRecognition import facial_expression as fe
from IntentIdentification import Intent_identifiction as ii
import time

def annotate(image):
    #image = fd.detectFace(image)
    #image,name = fr.recognizeFace(image)
    #image = od.detectObject(image)
    #image,predictions = sr.recognizeScene(image)
    image = fe.facialExpression(image)
    
    return image

def textual_data(text):
    start_time = time.time()
    text=ii.predict_intent(text)
    end_time = time.time()
    print(end_time-start_time)
    return text

print(textual_data("hello my name is maleeha, what will be the weather tommorrow"))
