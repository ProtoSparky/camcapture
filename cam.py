#remember to install pip install opencv-python
##and Pillow for PIL
settings_dir = "./settings.json"
static_img = "./assets/img/static.png"
timelapse_dir = "./assets/img/history/"
max_retries = 10 #how many times the camera can fail to capture before it will be reinitialized
import cv2
import pyassets.tools as tools 
import threading
import time
import atexit
from datetime import datetime
import os
from PIL import Image 
import sys

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
cam.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*settings["camera_mode"]))
cam.set(cv2.CAP_PROP_FRAME_WIDTH, int(settings["camera_res_x"]))
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, int(settings["camera_res_y"]))

def cleanup():
    print("Releasing cam")
    cam.release()
atexit.register(cleanup)

def continouscam(sleep_seconds, max_retries):
    current_retries = 0
    print("capturing fast")
    while True:
        ret, frame = cam.read()
        if ret:
            cv2.imwrite(static_img, frame)
        else:
            print("Failed to capture image")
            if(current_retries > max_retries):
                print("killing cam and reinitializing")
                exit(42069)
            else:
                current_retries += 1
        ##sleep for given amount
        time.sleep(sleep_seconds)

def slow_capture(sleep_seconds, max_retries):
    current_retries = 0
    while True:
        ret, frame = cam.read()        
        if ret:
            formatted_date = get_formatted_date()
            cv2.imwrite(timelapse_dir + formatted_date + ".png", frame)
            current_dir_size = tools.get_size_and_count("./assets/img/history/")
            current_storage = tools.open_json("./stats.json")
            current_storage["history_storage_size"] = current_dir_size[0]
            current_storage["history_size"] = current_dir_size[1]
            current_storage["last_slow_capture"] = formatted_date
            tools.write_json("./stats.json", current_storage)
        else:
            print("Failed to capture image")
            if(current_retries > max_retries):
                print("killing cam and reinitializing")
                exit(42069)
            else:
                current_retries += 1

        time.sleep(sleep_seconds)

def fps_to_sleep_time(fps):
    if fps <= 0:
        raise ValueError("FPS must be a positive number")    
    return 1 / fps

slow_capturefps = 3600/settings["constant_update_freq"]
fast_capture = fps_to_sleep_time(settings["burst_fps"])
slow_thread = threading.Thread(target=slow_capture, args=(slow_capturefps,max_retries,))
fast_thread = threading.Thread(target=continouscam, args=(fast_capture,max_retries,))
slow_thread.start()
fast_thread.start()
slow_thread.join()
fast_thread.join()
