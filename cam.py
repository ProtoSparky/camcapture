#remember to install pip install opencv-python
settings_dir = "./settings.json"
static_img = "./assets/img/static.png"

import cv2
import pyassets.tools as tools 
import http.server  
import socketserver
try:
    settings = tools.open_json(settings_dir)
except:
    print("Settings file missing! Run setup.py")
    exit()
tools.launch_html_server("./",4200)
# Initialize the camera
cam = cv2.VideoCapture(int(settings["cam_id"]))





# Capture a single frame
ret, frame = cam.read()

if ret:
    # Save the captured frame as an image
    cv2.imwrite(static_img, frame)
else:
    print("Failed to capture image")

# Release the camera
cam.release()


