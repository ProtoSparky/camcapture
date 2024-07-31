#this script is supposed to set up the environment for the camera capture
##remember to install apt get v4l2-ctl
import pyassets.tools as tools
import os
import subprocess
import re
settings_dir = "./settings.json"

def main(): 
    obj = {}
    eval1()
    obj["cam_id"] = eval2()
    print(obj)
    

    try:
        os.remove(settings_dir) #remove previous config
    except:
        print("cannot remove clear settings dir")




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
        return ids
    else:
        eval2()
    

        
    

def get_camera():
    result = subprocess.run(['v4l2-ctl', '--list-devices'], capture_output=True, text=True)
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
    

##start code
main()