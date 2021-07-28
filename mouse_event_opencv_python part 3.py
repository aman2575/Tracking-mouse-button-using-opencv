# -*- coding: utf-8 -*-
"""
Created on Wed Jul 28 10:53:28 2021

@author: aman
"""
# Opening color of the image in new_window
import numpy as np
import cv2 

#events = [i for i in dir(cv2) if  'EVENT' in i ]
#print(events)

def click_event(event, x,y,flags,param):
    if event == cv2.EVENT_LBUTTONDOWN:
        blue = img[x,y,0]
        green = img[x,y,1]
        red = img[x,y,2]
        cv2.circle(img,(x,y),3,(0,0,255),-1)
        mycolorImage = np.zeros((512,512,3),np.uint8)
        mycolorImage[:]=[blue,green,red]
        
        cv2.imshow('color',mycolorImage)

points=[]

#img = np.zeros((512,512,3), np.uint8)
img = cv2.imread('C:\\Users\\g1ama\\Desktop\\429.jpeg',1) 

cv2.imshow('image',img)

cv2.setMouseCallback('image',click_event)

cv2.waitKey(0) 
cv2.destroyAllWindows()