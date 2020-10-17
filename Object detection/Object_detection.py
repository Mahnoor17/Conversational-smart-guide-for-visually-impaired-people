from imageai.Detection import ObjectDetection
import cv2

def detectObject(image):
    """
    Takes image path as input and returns image with detected object
    
    """
    detector = ObjectDetection()

    model_path = "./models/yolo-tiny.h5"
    input_path = image
    output_path = "./output/newimage.jpg"

    detector.setModelTypeAsTinyYOLOv3()
    detector.setModelPath(model_path)
    detector.loadModel()
    detection = detector.detectObjectsFromImage(input_image=input_path, output_image_path=output_path)
    output=cv2.imread(output_path)
    cv2.imshow('Detected objects',output)
    cv2.waitKey(0)

    #probability of detected objects
    for eachItem in detection:
        print(eachItem["name"] , " : ", eachItem["percentage_probability"])
    return output

#calling this function
output_image=object_detection('./input/dining_table.jpg')



    