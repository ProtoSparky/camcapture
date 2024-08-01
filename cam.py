#remember to install pip install opencv-python
settings_dir = "./settings.json"
static_img = "./assets/img/static.png"
timelapse_dir = "./assets/img/history/"

import cv2
import pyassets.tools as tools 
import threading
import time
import atexit
from datetime import datetime

try:
    settings = tools.open_json(settings_dir)
except:
    print("Settings file missing! Run setup.py")
    exit()

def get_formatted_date():
    now = datetime.now()
    formatted_date = now.strftime("%Y-%m-%d-%H-%M")    
    return formatted_date

# Initialize the camera
cam = cv2.VideoCapture(int(settings["cam_id"]))
def cleanup():
    print("Releasing cam")
    cam.release()
atexit.register(cleanup)

def continouscam(sleep_seconds):
    print("capturing fast")
    while True:
        ret, frame = cam.read()
        if ret:
            print("f")
            cv2.imwrite(static_img, frame)
        else:
            print("Failed to capture image")
        ##sleep for given amount
        time.sleep(sleep_seconds)

def slow_capture(sleep_seconds):
    while True:
        ret, frame = cam.read()        
        if ret:
            print("s")
            cv2.imwrite(timelapse_dir + get_formatted_date() + ".png", frame)
        else:
            print("Failed to capture image")
        time.sleep(sleep_seconds)

def fps_to_sleep_time(fps):
    if fps <= 0:
        raise ValueError("FPS must be a positive number")    
    return 1 / fps


slow_thread = threading.Thread(target=slow_capture(3600/settings["constant_update_freq"]))
fast_thread = threading.Thread(target=continouscam(fps_to_sleep_time(settings["burst_fps"])))

slow_thread.join()
fast_thread.join()
slow_thread.start()
fast_thread.start()

