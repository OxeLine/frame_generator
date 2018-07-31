#!/usr/bin/env python3

import sys
import cv2
import keyboard as kb
import numpy as np

if len(sys.argv) == 1:
    print('Usage: ' + sys.argv[0] + ' (file to save)')
    exit(0)

cap = cv2.VideoCapture(sys.argv[1])

i = 0
data = []

while True:
    _, frame = cap.read()

    if frame is None:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    data.append(cv2.resize(gray, (160, 90)))
    i +=1
    if (i >= 3):
        data = []
        i = 0
    cv2.imshow('frame', frame)

    cv2.waitKey(1)
    if kb.is_pressed('q'):
        break

cap.release()
cv2.destroyAllWindows()