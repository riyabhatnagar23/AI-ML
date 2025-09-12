import cv2
from cvzone.HandTrackingModule import HandDetector
import numpy as np
import time
import math

cap = cv2.VideoCapture(0)
detector = HandDetector(maxHands=2)
offset = 20
imgSize=300
counter = 0

folder ="C:/Users/2020r/Desktop/jupyter miniProject/Indian-Sign-Language-Detection/data/1"

while True:
    success,img = cap.read()
    hands,img = detector.findHands(img)
    if hands:
        hand = hands[0]
        x,y,w,h = hand['bbox']

        imgwhite = np.ones((imgSize,imgSize,3),np.uint8)*255

        imgcrop = img[y-offset : y+h+offset ,x-offset : x+w+offset]

        imgcropshape = imgcrop.shape

        asspectratio = h/w  
        if asspectratio > 1:
            k=imgSize/h
            wcal = math.ceil(k*w)
            imgresize = cv2.resize(imgcrop, (wcal,imgSize))
            imgresizeshape = imgresize.shape
            wgap = math.ceil((imgSize- wcal)/2)
            imgwhite[: ,wgap: wcal+wgap] = imgresize

        else :
            k=imgSize/w
            hcal = math.ceil(k*h)
            imgresize = cv2.resize(imgcrop, (imgSize,hcal))
            imgresizeshape = imgresize.shape
            hgap = math.ceil((imgSize- hcal)/2)
            imgwhite[hgap : hcal+hgap ,: ] = imgresize

        cv2.imshow('ImageCrop',imgcrop)
        cv2.imshow('ImageWhite',imgwhite)

    cv2.imshow("Image",img)
    key = cv2.waitKey(1)
    if key == ord('s'):
        counter += 1
        cv2.imwrite(f'{folder}/Image_{time.time()}.jpg', imgwhite)
        print(counter)

