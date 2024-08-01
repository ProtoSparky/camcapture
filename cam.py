#remember to install pip install opencv-python
settings_dir = "./settings.json"
static_img = "./assets/img/static.png"

import cv2
import pyassets.tools as tools 
import http.server  
import socketserver
import time
import atexit


try:
    settings = tools.open_json(settings_dir)
except:
    print("Settings file missing! Run setup.py")
    exit()

# Initialize the camera
cam = cv2.VideoCapture(int(settings["cam_id"]))



def cleanup():
    print("Releasing cam")
    cam.release()
atexit.register(cleanup)

def continouscam(sleep_seconds):
    print("capturing")
    while True:
        ret, frame = cam.read()
        if ret:
            cv2.imwrite(static_img, frame)
        else:
            print("Failed to capture image")
        ##sleep for given amount
        time.sleep(sleep_seconds)
continouscam(0.1)