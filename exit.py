import psutil
import os
import signal

def kill_process_tree(parent_pid, sig=signal.SIGTERM):
    """Kill a process and all its children."""
    try:
        parent = psutil.Process(parent_pid)
    except psutil.NoSuchProcess:
        return
    children = parent.children(recursive=True)
    for child in children:
        try:
            child.send_signal(sig)
        except psutil.NoSuchProcess:
            continue
    try:
        parent.send_signal(sig)
    except psutil.NoSuchProcess:
        pass

def find_and_kill_process(script_name):
    """Find and kill the process running the specified script."""
    for proc in psutil.process_iter(['pid', 'name', 'cmdline']):
        try:
            # Check if the process is running the specified script
            if script_name in proc.info['cmdline']:
                print(f"Found process {proc.info['pid']} running {script_name}. Terminating...")
                kill_process_tree(proc.info['pid'])
                print(f"Process {proc.info['pid']} and its children terminated.")
                return
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            continue
    print(f"No process found running {script_name}.")

if __name__ == "__main__":
    script_to_kill = "./launch.py"
    find_and_kill_process(script_to_kill)
