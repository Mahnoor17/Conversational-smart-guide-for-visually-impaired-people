import face_recognition as fr
import numpy as np
from time import sleep
import os
import cv2

def registerFace():
    # For each person, enter one numeric face id
    face_id = input('\n enter your name ==>  ')
    print("\n [INFO] Initializing face capture. Look the camera and wait ...")
    cam = cv2.VideoCapture(0)
    cam.set(3, 640) # set video width
    cam.set(4, 480) # set video height
    face_detector = cv2.CascadeClassifier('haarcascades/haarcascade_frontalface_default.xml')
    # Initialize individual sampling face count
    count = 0
    while(True):
        ret, img = cam.read()
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = face_detector.detectMultiScale(gray, 1.3, 5)
        for (x,y,w,h) in faces:
            cv2.rectangle(img, (x,y), (x+w,y+h), (255,0,0), 2)     
            count += 1
        # Save the captured image into the datasets folder
            cv2.imwrite("faces/" + str(face_id) + ".jpg", gray[y:y+h,x:x+w])
            cv2.imshow('image', img)
        k = cv2.waitKey(100) & 0xff # Press 'ESC' for exiting video
        if k == 27:
            break
        elif count >= 1: # Take 30 face sample and stop video
            break
        cam.release()
        cv2.destroyAllWindows()
        
result=registerFace()

def get_encoded_faces():
    encoded={}
    for dirpath, dnames, fnames in os.walk('./faces'):
        for f in fnames:
            if f.endswith(".jpg") or f.endswith(".png"):
                face =  fr.load_image_file("faces/"+f)
                encoding = fr.face_encodings(face)[0]
                encoded[f.split(".")[0]] = encoding
    return encoded


def unknown_image_encoded(img):
    face =  fr.load_image_file("faces/"+f)
    encoding = fr.face_encodings(face)[0]
    return encodings

#def recognizeFace(image,rectangle):
def recognizeFace(image):
    faces = get_encoded_faces()
    face_encoded = list (faces.values())
    known_face_names = list (faces.keys())

    img= cv2.imread(image,1)

    face_locations=fr.face_locations(img)
    unknown_fac_encodings=fr.face_encodings(img,face_locations)

    face_names=[]
    for face_encoding in unknown_fac_encodings:
        matches = fr.compare_faces(face_encoded, face_encoding)
        name="Unknown"

        face_distances = fr.face_distance(face_encoded, face_encoding)
        best_match_index = np.argmin(face_distances)
        if matches[best_match_index]:
            name = known_face_names[best_match_index]
        
        face_names.append(name)

        for(top, right, bottom, left), name in zip(face_locations, face_names):
            cv2. rectangle(img, (left-20, top-10), (right+20, bottom+10), (255,0,0), 2)
            cv2. rectangle(img, (left-20, bottom -15), (right+20, bottom+10), (255,0,0), cv2.FILLED)
            font = cv2.FONT_HERSHEY_DUPLEX
            cv2.putText(img, name, (left-20, bottom -15), font, 1.0, (255,255,255),2)
            #cv2.putText(im,str(nbr_predicted)+"--"+str(conf), (x,y+h),font, 1.1, (0,255,0)) #Draw the text

    while True:
        cv2.imshow('Video',img)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            return face_names

print(recognizeFace('test.jpg'))
