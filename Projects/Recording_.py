# pip install opencv-python
# pip install pywin32
# pip install numpy
# pip install pyautogui

import cv2
import pyautogui
from win32api import GetSystemMetrics
import numpy as np
import time
width=GetSystemMetrics(0)
heigth=GetSystemMetrics(1)

dim=(width,heigth)
f=cv2.VideoWriter_fourcc(*"MJPG")
op=cv2.VideoWriter("test.mp4",f,30.0,dim)
start=time.time()
dur=10
end=start+dur
while True:
    img=pyautogui.screenshot()
    frames=np.array(img)
    frame=cv2.cvtColor(frames,cv2.COLOR_BGR2RGB)
    ctime=time.time()
    if ctime>end:
        break

op.release()
print("END")