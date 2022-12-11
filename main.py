import cv2
import os
from time import time
from WindowCapture import WindowCapture
from Vision import Vision

os.chdir(os.path.dirname(os.path.abspath(__file__)))
wincap = WindowCapture('METIN2')
vision_limestone = Vision("duygular.png")

loop_time = time()
while(True):
    screenshot = wincap.get_screenshot()
    points = vision_limestone.find(screenshot,0.60,'rectangle')
    print(f"FPS:{1/(time()-loop_time)}")
    loop_time = time()
    if cv2.waitKey(1) == ord('q'):
        cv2.destroyAllWindows()
        break
print("Done")
