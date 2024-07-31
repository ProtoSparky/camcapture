#remember to install pip install opencv-python
import cv2

# Initialize the camera
cam = cv2.VideoCapture(0    )

# Capture a single frame
ret, frame = cam.read()

if ret:
    # Save the captured frame as an image
    cv2.imwrite("snapshot.png", frame)
    print("Snapshot saved as snapshot.png")
else:
    print("Failed to capture image")

# Release the camera
cam.release()


