import numpy as np
import cv2 as cv
import pickle
from datetime import datetime
face_cascade = cv.CascadeClassifier('D:\\Django\\OpenCV\\Cascades\\data\\haarcascade_frontalface_alt2.xml')
recognizer = cv.face.LBPHFaceRecognizer_create()
recognizer.read("trainner.yml")

def markAttendance(name):
    with open('attendance.csv','r+') as f:
        myDataList = f.readlines()
        nameList = []
        for line in myDataList:
            entry = line.split(',')
            nameList.append(entry[0])
        if name not in nameList:
            now = datetime.now()
            dtString = now.strftime('%H:%M:%S')
            f.writelines(f'\n{name},{dtString}')

labels ={"person_name": 1}
with open("labels.pickle", 'rb') as f:
    og_labels = pickle.load(f)
    labels = {v:k for k,v in og_labels.items()}

cap = cv.VideoCapture(0)

while(True):
    # Capture frame-by-frame
    ret,frame = cap.read()
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale( gray,scaleFactor = 1.5, minNeighbors=5)
    for (x ,y, w, h) in faces:
        print(x, y, w, h)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = gray[y:y+h, x:x+w]
        
        #recognize? 
        id_,conf = recognizer.predict(roi_gray)
        if conf >=45:
            print(id_)
            print(labels[id_])
            font = cv.FONT_HERSHEY_SIMPLEX
            name = labels[id_]
            color = (255, 255, 255)
            stroke = 2 
            cv.putText(frame, name, (x,y), font, 1, color, stroke, cv.LINE_AA)
            markAttendance(name)
        img_item = "my-image.png"
        cv.imwrite(img_item, roi_gray)

        color=(255,0,0)
        stroke =2
        end_cord_x= x+w
        end_cord_y= y+h
        cv.rectangle(frame,(x,y),(end_cord_x,end_cord_y),color,stroke)

    cv.imshow('frame',frame)
    if cv.waitKey(20) & 0xFF == ord('q'):
        break






cap.release()
cv.destroyAllWindows()