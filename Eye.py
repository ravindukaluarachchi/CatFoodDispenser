#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  3 20:52:36 2021

@author: ravindu
"""

import cv2
from datetime import datetime
import ColorComparer

# Loading the cascades
face_cascade = cv2.CascadeClassifier('haarcascade_frontalcatface.xml')
homeCatFeatures = [(0.38, 0.53, 0.52), (0.12, 0.26, 0.22), (0.26, 0.44, 0.39)]
#[(0.3, 0.33, 0.3), (0.53, 0.56, 0.54), (0.8, 0.82, 0.79)]

# Defining a function that will do the detections
def detect(gray, frame):
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    if(len(faces) >0):
        print('Cat detected....')        
    for (x, y, w, h) in faces:
        #cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
        frame = frame[y:y+h, x:x+w]
        #roi_gray = gray[y:y+h, x:x+w]
        #roi_color = frame[y:y+h, x:x+w]        
    return frame, len(faces) >0

def match(face):
    colorFeatures = ColorComparer.detectColorFeatures(face)
    return ColorComparer.compare(homeCatFeatures, colorFeatures)

def open():
    global video_capture
    video_capture = cv2.VideoCapture(0)
    
def see():    
    _, frame = video_capture.read()    
    
    frame = cv2.flip(frame, 0)
    #cv2.imwrite(datetime.now().strftime('%H%M%S') + '_full.png', frame)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    canvas, detected = detect(gray, frame)
    
    #cv2.imshow('Video', canvas)
    #if cv2.waitKey(1) & 0xFF == ord('q'):
    #    break    
    #cv2.destroyAllWindows()
    matched = False
    if detected:        
        matched = match(canvas)
        print('Cat matched : ' + str(matched))
        if matched:
            cv2.imwrite('faces/captured/' + datetime.now().strftime('%H%M%S') + '_matched.png', canvas)
        else:
            cv2.imwrite('faces/captured/' + datetime.now().strftime('%H%M%S') + '_diff.png', canvas)        
    return matched

def close():
    video_capture.release()
    
def write():
    _, frame = video_capture.read()
    frame = cv2.flip(frame, 0)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    canvas, detected = detect(gray, frame)
    if detected:
        path = r'/media/ravindu/HDD1/Msc/Robotics/catface/faces/captured' + datetime.now().strftime('%H%M%S') + '.jpg'
        cv2.imwrite(path,canvas)