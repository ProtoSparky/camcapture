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
from PIL import Image 
import subprocess
import re
try:
    print("loading settings file")
    settings = tools.open_json(settings_dir)
except:
    print("Settings file missing! Run setup.py")
    exit()

def get_formatted_date():
    now = datetime.now()
    formatted_date = now.strftime("%Y-%m-%d-%H-%M")    
    return formatted_date

def get_camera():
    try:
        result = subprocess.run(['v4l2-ctl', '--list-devices'], capture_output=True, text=True)
    except:
        print("Failed to run v4l2-ctl', '--list-devices!. Have you installed v4l-utils?")
        
    lines = result.stdout.split('\n')    
    webcams = {}
    current_camera = None 
    for line in lines:
        if ':' in line and '/dev/video' not in line:
            current_camera = line.split(':')[0].strip()
            webcams[current_camera] = []
        else:
            match = re.search(r'/dev/video(\d+)', line)
            if match and current_camera is not None:
                webcams[current_camera].append(int(match.group(1)))    
    webcams = {k: v for k, v in webcams.items() if v}    
    return webcams


def get_camera_display_modes(camera_id):
    try:
        # Run the command to list formats for the specified camera
        result = subprocess.run(['v4l2-ctl', '-d', '/dev/video'+str(camera_id),'--list-formats-ext'], capture_output=True, text=True)
    except:
        print("Failed to run v4l2-ctl', '--list-devices!. Have you installed v4l-utils?")
        exit()
    output = result.stdout

    # Initialize the dictionary to store the parsed data
    parsed_data = {
        "MJPG": [],
        "YUYV": []
    }

    # Regular expressions to match the format and resolutions
    format_regex = r"\[(\d+)\]: '(\w+)'"
    resolution_regex = r"Size: Discrete (\d+x\d+)"

    current_format = None

    # Iterate through the lines of the output
    for line in output.split('\n'):
        format_match = re.search(format_regex, line)
        if format_match:
            format_name = format_match.group(2)
            if format_name == "MJPG":
                current_format = "MJPG"
            elif format_name == "YUYV":
                current_format = "YUYV"
        
        resolution_match = re.search(resolution_regex, line)
        if resolution_match and current_format:
            resolution = resolution_match.group(1)
            if resolution not in parsed_data[current_format]:
                parsed_data[current_format].append(resolution)

    return parsed_data  

def get_set_cam_id():
    #function tries to find id from camera name, mode and resolution
    cameras = get_camera()
    #try to select camera from settings
    try:
        select_cam_ids = cameras[settings["cam_name"]]
    except:
        print("Camera with name given in settings does not exist!")
        exit()
    
    #iterate trough all ids and find the given resolution that was selected
    for selected_id in select_cam_ids:
        select_display_modes = get_camera_display_modes(selected_id)
        #try to select display mode
        try:
            cam_display_resolutions = select_display_modes[settings["camera_mode"]]
        except:
            print("Camera mode in settings does not match with actual camera!")
            exit()
        composite_res = str(settings["camera_res_x"]) + "x" + str(settings["camera_res_y"])
        if(composite_res in cam_display_resolutions):
            return int(selected_id)
        else:
            print("Camera id not found as resolution does not match camera capabilities!")
            exit()


# Initialize the camera
cam = cv2.VideoCapture(get_set_cam_id())
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
    Run = True
    while Run:
        ret, frame = cam.read()
        if ret:
            cv2.imwrite(static_img, frame)
        else:
            print("Failed to capture image")
            if(current_retries > max_retries):
                print("killing cam and reinitializing")
                Run = False
                break
            else:
                current_retries += 1
        ##sleep for given amount
        time.sleep(sleep_seconds)
    print("uwu_fast")
    exit()

def slow_capture(sleep_seconds, max_retries, sleep_seconds_fast):
    current_retries = 0
    frame_counter = 0
    capture_frame = sleep_seconds/sleep_seconds_fast
    Run = True
    while Run:
        ret, frame = cam.read()        
        if ret:
            formatted_date = get_formatted_date()
            cv2.imwrite(timelapse_dir + formatted_date + ".png", frame)
            current_dir_size = tools.get_size_and_count("./assets/img/history/")
            current_storage = {}
            current_storage["history_storage_size"] = current_dir_size[0]
            current_storage["history_size"] = current_dir_size[1]
            current_storage["last_slow_capture"] = formatted_date
            tools.write_json("./stats.json", current_storage)
        else:
            print("Failed to capture slow image")
            if(current_retries > max_retries):
                print("killing cam and reinitializing")
                Run = False
                break
            else:
                current_retries += 1
        frame_counter += 1
        time.sleep(sleep_seconds_fast)
    print("uwu_slow")
    exit()


def fps_to_sleep_time(fps):
    if fps <= 0:
        raise ValueError("FPS must be a positive number")    
    return 1 / fps

slow_capturefps = 3600/settings["constant_update_freq"]
fast_capture = fps_to_sleep_time(settings["burst_fps"])
slow_thread = threading.Thread(target=slow_capture, args=(slow_capturefps,max_retries,fast_capture, ))
fast_thread = threading.Thread(target=continouscam, args=(fast_capture,max_retries,))
slow_thread.start()
fast_thread.start()
slow_thread.join()
fast_thread.join()
