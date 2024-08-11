import psutil
import os
import signal

def kill_process_tree(pid, sig=signal.SIGTERM):
    """Kill a process tree (including grandchildren) with signal"""
    try:
        parent = psutil.Process(pid)
    except psutil.NoSuchProcess:
        return

    children = parent.children(recursive=True)
    for child in children:
        try:
            child.send_signal(sig)
        except psutil.NoSuchProcess:
            pass

    try:
        parent.send_signal(sig)
    except psutil.NoSuchProcess:
        pass

def find_and_kill_launch_script():
    # Iterate over all running processes
    for proc in psutil.process_iter(['pid', 'name', 'cmdline']):
        try:
            # Check if this process is the launch.py script
            if 'python3' in proc.info['name'] and ' launch.py' in proc.info['cmdline']:
                print(f"Found process {proc.info['pid']} running launch.py")
                # Kill the process tree
                kill_process_tree(proc.info['pid'])
                print(f"Killed process {proc.info['pid']} and its children")
                return
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass

    print("No running instance of launch.py found.")

if __name__ == "__main__":
    find_and_kill_launch_script()
