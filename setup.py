#this script is supposed to set up the environment for the camera capture
##remember to install apt get v4l2-ctl
#remember to install pip install opencv-python
##and Pillow for PIL
import pyassets.tools as tools
import os
import subprocess
import re
settings_dir = "./settings.json"

def main(): 
    obj = {}
    eval1()
    obj["cam_id"] = eval2()
    mode_and_res = eval7(obj["cam_id"])
    obj["camera_mode"] = mode_and_res[0]
    obj["camera_res_x"] = int(mode_and_res[1])
    obj["camera_res_y"] = int(mode_and_res[2])
    obj["constant_update_freq"] = eval3()
    obj["burst_fps"] = eval4()
    obj["web_port"] = eval5()
    obj["rotate_frame"] = eval6()

    try:
        os.remove(settings_dir) #remove previous config
    except:
        print("Settings file missing")
    tools.write_json(settings_dir, obj)
    print("Data written to settings file")
    exit()

def question(input_str, clear_term = True):
    if(clear_term):
        tools.Clear_Term()
    return input(input_str)


def eval1():
    q1 = question("start setup?(y/n). Starting will overwrite settings.json ")
    if(q1 == "y" or q1 == "Y"):
        return True
    elif(q1 == "n" or q1 == "N"):
        print("exiting!")
        exit()
    else:
        eval1()

def eval2():
    tools.Clear_Term()
    all_cameras = get_camera()
    cameras = all_cameras.keys()
    print("If nothing shows up here, run as sudo!")
    print("Select one of the following ids")
    tmp_camera_ids = []
    for current_camera in cameras:
        print("\n------" + current_camera + "------")
        print("ids: ")
        current_cam_obj = all_cameras[current_camera]
        for current_id in current_cam_obj:
            tmp_camera_ids.append(str(current_id))
            print(str(current_id))
    ids = question("Select one of the ids: ", False)
    if(ids in tmp_camera_ids):
        return int(ids)
    else:
        eval2()

def eval3():
    update_freq = question("Enter constant frames pr hour for history saving: ") 
    try:
       update_freq = float(update_freq)
       return update_freq
    except:
        eval3()


def eval4():
    update_freq = question("Enter preview stream fps ") 
    try:
       update_freq = float(update_freq)
       return update_freq
    except:
        eval4()
    
def eval5():
    port_number = question("Enter webserver port number: ")
    try:
        return int(port_number)
    except:
        eval5()

def eval6():
    rotate_by = question("Rotate viewport by x degrees 0-360): ")
    try:
        return int(rotate_by)
    except:
        eval6()

def eval7(id):
    tools.Clear_Term()
    camera_modes  = get_camera_display_modes(id)
    for current_cam_mode in camera_modes:
        print("\n---" + current_cam_mode + "---")
        for current_res in camera_modes[current_cam_mode]:
            print(current_res) 
    print("\n")
    try:
        codec, res = question("Enter camera res and mode. Valid input is mode+res (MJPG 1920x1080)",clear_term = False).split(" ", 1)
        if(res in camera_modes[codec]):
            width, height = res.split("x")
            return codec, width, height
        else:
            eval7(id)
    except:
        eval7(id)







        
    

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
    

    


##start code
main()