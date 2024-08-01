#!/usr/bin/env python3
import multiprocessing
import subprocess

def run_script(script_name):
    subprocess.run(["python3", script_name])

if __name__ == "__main__":
    # List of scripts to run
    scripts =        ["./cam.py", "./webserver.py"]

    # Create a process for each script
    processes = []
    for script in scripts:
        process = multiprocessing.Process(target=run_script, args=(script,))
        processes.append(process)
        process.start()

    # Wait for all processes to complete
    for process in processes:
        process.join()

    print("All scripts have finished executing.")