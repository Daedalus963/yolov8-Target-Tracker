<<<<<<< HEAD
# src/main.py
import os
import cv2
import time
from simulation.drone_simulator import DroneSimulator
from detection.detector import Detector

# Get the project root directory (one level up from src)
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
model_path = os.path.join(project_root, "models", "yolov8x.pt")
video_path = os.path.join(project_root, "models", "Test.mp4")

print("Model Path:", model_path)
print("Video Path:", video_path)

simulator = DroneSimulator(video_path=video_path)
simulator.start_simulation()
detector = Detector(model_path)

TARGET_CLASSES = ["car", "bus", "truck", "motorbike", "bicycle", "person"]

prev_time = 0
while True:
    frame = simulator.get_frame()
    if frame is None:
        print("Video ended. Exiting.")
        break
    outs = detector.detect(frame)
    print(f"[DEBUG] Frame processed. Number of detections: {len(outs.boxes)}")
    frame = detector.draw(frame, outs)
    # FPS calculation
    curr_time = time.time()
    fps = 1 / (curr_time - prev_time) if prev_time else 0
    prev_time = curr_time
    cv2.putText(frame, f"FPS: {fps:.2f}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
    cv2.imshow("Drone Object Detection", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

=======
# src/main.py
import os
import cv2
import time
from simulation.drone_simulator import DroneSimulator
from detection.detector import Detector

# Get the project root directory (one level up from src)
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
model_path = os.path.join(project_root, "models", "yolov8x.pt")
video_path = os.path.join(project_root, "models", "Test.mp4")

print("Model Path:", model_path)
print("Video Path:", video_path)

simulator = DroneSimulator(video_path=video_path)
simulator.start_simulation()
detector = Detector(model_path)

TARGET_CLASSES = ["car", "bus", "truck", "motorbike", "bicycle", "person"]

prev_time = 0
while True:
    frame = simulator.get_frame()
    if frame is None:
        print("Video ended. Exiting.")
        break
    outs = detector.detect(frame)
    print(f"[DEBUG] Frame processed. Number of detections: {len(outs.boxes)}")
    frame = detector.draw(frame, outs)
    # FPS calculation
    curr_time = time.time()
    fps = 1 / (curr_time - prev_time) if prev_time else 0
    prev_time = curr_time
    cv2.putText(frame, f"FPS: {fps:.2f}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
    cv2.imshow("Drone Object Detection", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

>>>>>>> b8ec38ba44cb6dc0ebafeeed30fd5ad860701c64
cv2.destroyAllWindows()