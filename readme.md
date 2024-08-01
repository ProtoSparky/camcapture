## Webcamera capture

These python scripts will help you display a webcam feed on a webserver, save feed snapshots on an hourly basis, and show a "live" feed on the web interface. 

To get started, install the dependencies, and run Setup.py as sudo to set up the other scripts. Once that's completed, run Launch.py as sudo. 

The reason for it needing sudo is that some systems cant access the webcams without sudo. (I have no idea how do make it sudo free for all occasions)

### Dependencies
* v4l2-ctl (can be installed with sudo apt install v4l2-ctl)
* opencv-python (installed with pip install opencv-python)
* Pillow (-||-)

## Setup (also a list of features)
Launch setup.py with sudo
The setup will ask you for a given camera id. You'll see a list of them for all cameras plugged into your system. 
You'll be able to select the resolution and mode of the camera.
After this, it'll ask you to select the preview image fps, and frames pr hour for the historical images.
In the end, you'll be able to rotate the "live" feed by whatever angle you want.
That's it :3

### How 2 run Launch.py? 
There are primarily 2 ways you can do i. For testing i recommend you run it using the first method.
* Running it normally ```sudo python3 ./launch.py```
* Running it in background with ```sudo nohup python3 ./launch.py &```

