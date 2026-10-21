#pylint:disable=no-member

import os    #Import the libraries
import cv2 as cv
import numpy as np

people = [
    'ben_afflek',
    'elton_john',
    'jerry_seinfeld',
    'madonna',
    'mindy_kaling'
]
DIR = r'Media Files\data\train'

haar_cascade = cv.CascadeClassifier(
    cv.data.haarcascades + "haarcascade_frontalface_default.xml"
)  #Load the Haar Cascade model

features = []  #reate the empty list
labels = []

def create_train():     #create the train function
    for person in people:
        path = os.path.join(DIR, person)
        label = people.index(person)

        for img in os.listdir(path):  #Read every image inside each person's folder
            img_path = os.path.join(path,img)

            img_array = cv.imread(img_path)
            if img_array is None:
                continue 
                
            gray = cv.cvtColor(img_array, cv.COLOR_BGR2GRAY)  #Convert the image to grayscale

            faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=4)  #Detect faces using Haar Cascade

            for (x,y,w,h) in faces_rect:  #Crop the detected face and save its label
                faces_roi = gray[y:y+h, x:x+w]
                features.append(faces_roi)
                labels.append(label)

create_train()    #Run the function
print('Training done ---------------')

features = np.array(features, dtype='object')  #Convert the lists to NumPy arrays
labels = np.array(labels)

face_recognizer = cv.face.LBPHFaceRecognizer_create()  #Create the LBPH recognizer

# Train the Recognizer on the features list and the labels list
face_recognizer.train(features,labels)

face_recognizer.save('face_trained.yml')  #s
np.save('features.npy', features)
np.save('labels.npy', labels)