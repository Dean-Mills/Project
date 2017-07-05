# -*- coding: utf-8 -*-
"""
Created on Tue Jul  4 13:11:57 2017

@author: dean
"""

import cv2
import numpy as np

VideoFeed = cv2.VideoCapture(0)

while True:
    ret, frame = VideoFeed.read()
    cv2.imshow('frame', frame)
    
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
        
VideoFeed.release()
cv2.destroyWindow(frame)
cv2.waitKey(-1)