# src/detection/detector.py
from ultralytics import YOLO
import cv2
import numpy as np

TARGET_CLASSES = ["car", "bus", "truck", "motorbike", "bicycle", "person"]  # Add your target classes here

class Detector:
    def __init__(self, model_path, *args, **kwargs):
        self.model = YOLO(model_path)  # Use YOLOv8 model
        self.classes = self.model.names  # dict: {class_id: class_name}

    def detect(self, frame):
        # Run inference on the frame
        results = self.model(frame, verbose=False)[0]
        return results

    def draw(self, frame, results):
        # results.boxes: boxes.xyxy, boxes.conf, boxes.cls
        for box, conf, cls_id in zip(results.boxes.xyxy, results.boxes.conf, results.boxes.cls):
            if conf < 0.6:  # Adjust threshold as needed
                continue
            label = self.classes[int(cls_id)]
            if label not in TARGET_CLASSES:
                continue
            x1, y1, x2, y2 = map(int, box)
            color = (0, 0, 255)  # Bright red for maximum visibility
            thickness = 2  # Reduced thickness for bounding box
            cv2.rectangle(frame, (x1, y1), (x2, y2), color, thickness)
            cv2.putText(frame, f"{label}: {conf:.2f}", (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 1.2, color, 2)
            print(f"Drawing box: {label} ({conf:.2f}) at [{x1},{y1},{x2},{y2}]")
        return frame