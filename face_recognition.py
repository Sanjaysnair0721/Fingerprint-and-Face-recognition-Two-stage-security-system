import cv2
import os
import numpy as np

img=cv2.imread('2.png',0);
img=cv2.imread('1.png',0);
subjects = ["", "Sanjay S Nair", "Your Name"]
def detect_face(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    face_cascade = cv2.CascadeClassifier('opencv-files/lbpcascade_frontalface.xml')
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=5);
    
    if (len(faces) == 0):
        return None, None
    (x, y, w, h) = faces[0]
    return gray[y:y+w, x:x+h], faces[0]

def prepare_training_data(data_folder_path):
    dirs = os.listdir(data_folder_path)
    faces = []
    labels = []
    
    for dir_name in dirs:
        if not dir_name.startswith("s"):
            continue;
    
        label = int(dir_name.replace("s", ""))
        subject_dir_path = data_folder_path + "/" + dir_name
        subject_images_names = os.listdir(subject_dir_path)
    
        for image_name in subject_images_names:
            if image_name.startswith("."):
                continue;
            image_path = subject_dir_path + "/" + image_name

            image = cv2.imread(image_path)
            #cv2.imshow("Training on image...", cv2.resize(image, (400, 500)))
            cv2.waitKey(100)
        
            face, rect = detect_face(image)
            if face is not None:
                faces.append(face)
                labels.append(label)
            
    cv2.destroyAllWindows()
    cv2.waitKey(1)
    cv2.destroyAllWindows()
    return faces, labels

print("Preparing data...")
faces, labels = prepare_training_data("training-data")
print("Data prepared")

print("Total faces: ", len(faces))
print("Total labels: ", len(labels))

face_recognizer = cv2.face.LBPHFaceRecognizer_create()
face_recognizer.train(faces, np.array(labels))

def draw_rectangle(img, rect):
    (x, y, w, h) = rect
    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)
    
def draw_text(img, text, x, y):
    cv2.putText(img, text, (x, y), cv2.FONT_HERSHEY_PLAIN, 1.5, (0, 255, 0), 2)
    if text =='Sanjay S Nair':
        img=cv2.imshow('1.png',0);
    elif text =='Your Name':
        img=cv2.imshow('2.png',0);
    else:
        print("face not recognised")
        
def predict(test_img):
    img = test_img
    face, rect = detect_face(img)
    flag = 0
    if face is None:
        flag = 1
        return img, flag
    label, confidence = face_recognizer.predict(face)
    if label is None:
        flag = 1
        return img, flag
    label_text = subjects[label]
    draw_rectangle(img, rect)
    draw_text(img, label_text, rect[0], rect[1]-5)
    
    return img, flag

test_img1 = cv2.imread("test-data/test1.jpg")
print("Predicting images...")
cap = cv2.VideoCapture(1)
counter = 0
while(True):
    if counter<200:
        counter=counter+1
        continue
    
    ret, frame = cap.read()
    if not frame is None:
        if not ret:
            continue
    test_img2 = frame
    cv2.resize(frame,(400, 500))

    predicted_img2, stat = predict(test_img2)
    if stat == 1:
        cv2.imshow(subjects[2],cv2.resize(frame,(400, 500)))
        continue
    cv2.imshow(subjects[1], cv2.resize(predicted_img2, (400, 500)))
    
    key = cv2.waitKey(1) & 0xFF
    if key == ord("q"):
        breakpoint
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.waitKey(1)
cv2.destroyAllWindows()






