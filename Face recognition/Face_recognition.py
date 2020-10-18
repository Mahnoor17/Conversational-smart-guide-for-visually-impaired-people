import face_recognition as fr
import numpy as np
from time import sleep
import os
import cv2

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


def registerFace(image,rectangle,name):
    return 0


print(recognizeFace('test.jpg'))