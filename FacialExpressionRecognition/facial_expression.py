import numpy as np
import cv2
import tensorflow as tf
def facialExpression(img):
    face_detection = cv2.CascadeClassifier('haar_cascade_face_detection.xml')
    #img = cv2.imread('faces.jpg')
    settings = {
        'scaleFactor': 1.3, 
        'minNeighbors': 5, 
        'minSize': (50, 50)
    }

    labels = ["Neutral","Happy","Sad","Surprise","Angry"]
    model = tf.keras.models.load_model('expression.model')
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    detected = face_detection.detectMultiScale(gray, **settings)
        
    for x, y, w, h in detected:
        cv2.rectangle(img, (x, y), (x+w, y+h), (245, 135, 66), 2)
        cv2.rectangle(img, (x, y), (x+w//3, y+20), (245, 135, 66), -1)
        face = gray[y+5:y+h-5, x+20:x+w-20]
        face = cv2.resize(face, (48,48)) 
        face = face/255.0
                    
    predictions = model.predict(np.array([face.reshape((48,48,1))])).argmax()
    state = labels[predictions]
    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(img,state,(x+10,y+15), font, 0.5, (255,255,255), 2, cv2.LINE_AA)
                    
    cv2.imshow('Facial Expression', img)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    #writer.writeFrame(img)
    return img

