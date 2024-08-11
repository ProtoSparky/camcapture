## CamCapture

These python scripts will help you display a webcam feed on a webserver, save feed snapshots on an hourly basis, and show a "live" feed on the web interface. 

To get started, install the dependencies, and run ```./launch.sh```

### Dependencies
* v4l2-ctl (can be installed with sudo apt install v4l-utils)
* opencv-python (installed with pip install opencv-python)
* Pillow (-||-)

## Setup (also a list of features)
Launch ```./launch.sh```
Select option 3 to start the setup process. It will ask you for a given camera id. You'll see a list of them for all cameras plugged into your system. 
You'll be able to select the resolution and mode of the camera.
After this, it'll ask you to select the preview image fps, and frames pr hour for the historical images.
In the end, you'll be able to rotate the "live" feed by whatever angle you want.
That's it :3

## Starting and stopping CamCapture
Run the same launch script, but then select either option 1 or 2 to launch or kill the software.
After stopping the program, youll be able to review the logs for any issues that might have popped up while it was running. 

