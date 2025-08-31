# src/simulation/drone_simulator.py
import numpy as np
import cv2
import os

class DroneSimulator:
    def __init__(self, video_path=None):
        self.is_running = False
        if video_path:
            self.cap = cv2.VideoCapture(video_path)
            if not self.cap.isOpened():
                print(f"Failed to open video file: {video_path}")
        else:
            self.cap = cv2.VideoCapture(0)  # 0 for webcam

    def start_simulation(self):
        self.is_running = True
        print("Drone simulation started.")

    def get_frame(self):
        if not self.is_running:
            raise RuntimeError("Simulation is not running. Start the simulation first.")
        ret, frame = self.cap.read()
        if not ret or frame is None:
            print("[DEBUG] End of video or cannot fetch frame. Restarting video.")
            self.cap.set(cv2.CAP_PROP_POS_FRAMES, 0)  # Restart video
            ret, frame = self.cap.read()
            if not ret or frame is None:
                print("[DEBUG] Still cannot fetch frame after restart. Returning None.")
                return None  # If still can't read, return None
        print(f"[DEBUG] Frame fetched. Shape: {frame.shape if frame is not None else None}")
        return frame

    def __del__(self):
        if hasattr(self, 'cap') and self.cap.isOpened():
            self.cap.release()

# Test code (to be removed or commented out in production)
# (Test code removed for production use)

# Main code (for running the simulation and detection)
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
video_path = os.path.join(project_root, "models", "Test.mp4")
print("Trying to open video:", video_path)
simulator = DroneSimulator(video_path=video_path)
simulator.start_simulation()
while True:
    frame = simulator.get_frame()
    if frame is None:
        print("Video ended. Exiting.")
        break
    cv2.imshow("Drone Object Detection", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cv2.destroyAllWindows()