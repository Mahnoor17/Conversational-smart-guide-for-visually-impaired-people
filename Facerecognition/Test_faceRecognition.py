import Face_recognition as fr
import cv2
import os

def load_images_from_folder(folder):
    images = []
    img_names=[]
    for filename in os.listdir(folder):
        img = cv2.imread(os.path.join(folder,filename))
        img_name=filename.split(".")[0]
        img_names.append(img_name)
        if img is not None:
            images.append(img)
    return (images,img_names)


def test_faceDetection(images):
    names=[]
    images_list=[]
    for i in range(len(images)):
        image,name=fr.recognizeFace(images[i])
        images_list.append(image)
        print(name)
        names.append(name)
    return (images_list,names)


def confusion_matrix(names,actual_names):
    TP=FP=TN=FN=0
    for i in range(len(names)):
        if names[i]==actual_names[i]:
            TP=TP+1
        elif (names[i]=='Unknown') & ('Unknown' in actual_names[i]):
            TN=TN+1
        elif (names[i]=='Unknown') & ('Unknown' not in actual_names[i]):
            FN=FN+1
        else:
            FP=FP+1
    acc=(TP+TN)/(TP+FP+FN+TN)
    precision = TP/(TP+FP)
    recall = TP/(TP+FN)
    f1_score = 2*(recall * precision) / (recall + precision)
    return (acc,precision,recall,f1_score)

images,actual_names = load_images_from_folder('test')
images,names = test_faceDetection(images)
print(confusion_matrix(names,actual_names))
