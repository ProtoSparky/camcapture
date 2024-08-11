#!/usr/bin/env python3
import multiprocessing
import subprocess
import time

def runner(script_name):
    while True:
        print(f"Starting {script_name}")
        process = subprocess.run(["python3", script_name])
        print(f"{script_name} exited with return code {process.returncode}")
        if script_name == "./cam.py":
            print(f"Restarting {script_name}...")
            time.sleep(1)

if __name__ == "__main__":
    scripts = ["./cam.py", "./webserver.py"]
    
    processes = []
    for script in scripts:
        process = multiprocessing.Process(target=runner, args=(script,))
        processes.append(process)
        process.start()

    # Wait for all processes to complete
    for process in processes:
        process.join()
