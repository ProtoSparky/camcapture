#!/bin/bash
# Function to check if the script is running with sudo
check_sudo() {
  if [ "$EUID" -ne 0 ]; then
    echo "This script requires sudo privileges. Restarting with sudo..."
    exec sudo bash "$0" "$@"
  fi
}

# Call the check_sudo function at the start
check_sudo "$@" 

launch_script() {
    # Start the process in a new session and redirect output
    setsid nohup python3 ./cam_daemon.py > launch.log 2>&1 &
    echo $! > launch.pid

    webserver_port=$(jq -r '.web_port' ./settings.json)
    echo "CamCapture launched in the background with PID $(cat launch.pid) and port number $webserver_port."
}

kill_script() {
    if [ -f "launch.pid" ]; then
        PID=$(cat launch.pid)
        # Kill the entire process group
        kill -TERM -- -$(ps -o pgid= -p $PID | grep -o '[0-9]*')
        rm launch.pid
        echo "Python script and its children have been terminated."
    else
        echo "No running script found."
    fi
}


setup(){
    sudo python3 ./setup.py
}

install_dependencies+setup(){
    apt update
    apt install v4l-utils
    apt install python3-pip
    pip install opencv-python
    pip install pillow
    setup
}

while true; do
    echo "Choose an option:"
    echo "1) Launch CamCapture"
    echo "2) Kill/stop CamCapture"
    echo "3) Setup CamCapture"
    echo "4) Install dependencies and setup"
    echo "5) Exit"
    read -p "Enter your choice: " choice

    case $choice in
        1)
            clear
            launch_script
            ;;
        2)
            clear
            kill_script
            ;;
        3)
            setup
            ;;
        4)
            install_dependencies+setup
            ;;

        5)
            echo "Exiting"
            exit 0
            ;;

        *)
            echo "Invalid option. Please try again."
            ;;
    esac
done
