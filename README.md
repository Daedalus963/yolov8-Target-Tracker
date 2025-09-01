# YOLOv8 Target Tracker – Aerial Object Detection

![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)
![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)
![Build Status](https://img.shields.io/badge/build-passing-brightgreen)

Welcome! This project helps you detect **cars, vehicles, people, and animals** in aerial/drone footage using YOLOv8.

---


## Table of Contents
- [Features](#features)
- [Requirements](#requirements)
- [Project Overview](#project-overview)
- [Installation](#installation)
- [How to Run](#how-to-run)
- [Example Outputs](#example-outputs)
- [Project Structure](#project-structure)
- [Future Improvements](#future-improvements)
- [Who is this for?](#who-is-this-for)
- [Questions or Feedback](#questions-or-feedback)
- [License](#license)

---


## 🚀 Features

- Real-time object detection from aerial/drone footage
- Supports custom or pre-recorded video input
- Modular code structure for easy extension
- FPS display and bounding box annotation
- Sample outputs for quick evaluation

---

## ⚙️ Requirements

- Python 3.8+
- OpenCV
- Ultralytics YOLOv8
- Windows, macOS, or Linux

Install dependencies using the provided `requirements.txt`.

---

## 📌 Project Overview

This system uses the **Ultralytics YOLOv8 model** and **OpenCV** to detect objects from **simulated drone videos**.  
It processes each video frame in real-time, draws bounding boxes with class labels, and displays frame rate (**FPS**) for performance tracking.

---

## 🛠️ Installation

1. **Clone the repository**
	```bash
	git clone https://github.com/Daedalus963/yolov8-target-tracker.git
	cd yolov8-target-tracker
	```

2. **(Optional) Create a virtual environment**
	```bash
	python -m venv venv
	# On macOS/Linux
	source venv/bin/activate
	# On Windows
	venv\Scripts\activate
	```

3. **Install dependencies**
	```bash
	pip install -r requirements.txt
	```

---


## 🚀 How to Run

1. **Add your video file**
	- Place your aerial video in the `models` folder as `Test.mp4`.
	- To use a different file, update the path in `src/main.py`.

2. **Run the detection script**
	```bash
	python src/main.py
	```

3. **Controls**
	- Press `Q` to quit the video window.

---


## 📊 Example Outputs

Here’s what you can expect when the model runs:

| Frame with Detections | Description |
|-----------------------|-------------|
| ![Sample Output 1](models/sample_output_1.png) | Bounding boxes for cars, buses, people, and animals displayed in real-time with FPS counter. |
| ![Sample Output 2](models/sample_output_2.jpg) | Real-time bounding boxes with FPS counter. |
| ![Sample Output 3](models/sample_output_3.png) | Detection of multiple object classes in a single frame. |

---


## 📂 Project Structure

```
yolov8-target-tracker/
│
├── README.md                # 📖 Project documentation
├── .gitignore               # 🚫 Ignored files (caches, temp files, etc.)
├── requirements.txt         # 📦 Python dependencies
│
├── models/                  # 🧩 Model files and sample outputs
│   ├── coco.names           #   Class labels for detection
│   ├── sample_output_1.png  #   Example detection result
│   ├── sample_output_2.jpg  #   Example detection result
│   └── sample_output_3.png  #   Example detection result
│
└── src/                     # 🏗️ Source code
    ├── main.py              #   Main entry point
    ├── detection/           #   Detection module
    │   └── detector.py      #     YOLOv8 detector logic
    └── simulation/          #   Drone simulation module
        └── drone_simulator.py #   Simulated drone video feed
```

---

## 🔮 Future Improvements

- Custom-trained YOLOv8 weights
- Object tracking (DeepSORT, ByteTrack)
- Web application deployment

---


## 🤝 Who is this for?

- Students and researchers in computer vision
- Drone enthusiasts
- Anyone interested in real-time object detection


---

## 📬 Questions or Feedback

- Email: deekshithas369@gmail.com
- GitHub Issues: [Open an issue](https://github.com/Daedalus963/yolov8-target-tracker/issues)

---

## 📜 License


Licensed under the [MIT License](LICENSE).
