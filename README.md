# **YOLOv8 Target Tracker – Aerial Object Detection**

![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)
![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)
![Build Status](https://img.shields.io/badge/build-passing-brightgreen)

Welcome! My name is **DEEKSHITHA SOMASHEKHAR**, and I’m excited to share this project with you.

`YOLOv8 Target Tracker` is a user-friendly, real-time object detection system built to help you spot **cars, vehicles, people, and animals** from aerial or drone footage. Whether you’re interested in surveillance, traffic analysis, or wildlife monitoring, this tool aims to make detection simple, fast, and reliable.

---
## **📌 Project Overview**

This project uses **Ultralytics YOLOv8** for real-time object detection from aerial perspectives. Here’s what’s inside:
- **Drone simulation module** for video feeds
- **Detector module** powered by YOLOv8
- Real-time FPS display and annotated bounding boxes for detected objects

I’ve designed this to be approachable for both beginners and experienced users. If you’re curious about computer vision or want to automate aerial monitoring, you’re in the right place!

---
## **🛠️ Installation**

Getting started is easy! Just follow these steps:

**1️⃣ Clone the repository**
```bash
git clone https://github.com/YOUR_USERNAME/yolov8-target-tracker.git
cd yolov8-target-tracker
```

**2️⃣ (Optional) Create a virtual environment**
```bash
python -m venv venv
# On macOS/Linux
source venv/bin/activate
# On Windows
venv\Scripts\activate
```

**3️⃣ Install dependencies**
```bash
pip install -r requirements.txt
```

---
## **🚀 How to Run the Project**

Ready to see it in action?

**1️⃣ Add your video file**
Place your aerial video in the `models` folder and name it `Test.mp4`. (Or, update the path in `src/main.py` to use a different file.)

**2️⃣ Run the detection script**
```bash
python src/main.py
```

**3️⃣ Controls**
- Press **`Q`** to quit the video display window.

---
## **📊 Example Outputs**

Here’s a quick preview of what you’ll see:

| Frame with Detections                                                        | Description                                                                                      |
| ---------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------ |
| ![Sample Output]
c:\Users\Deekshitha S\Pictures\Screenshots\Screenshot 2025-06-18 135235.png
| Bounding boxes for **cars, buses, people, and animals** displayed in real-time with FPS counter. |

--- 
## **📂 Project Structure**

Here’s a quick look at how the project is organized:
```
yolov8-target-tracker/
│
├── README.md
├── .gitignore
├── requirements.txt
├── models/
│   └── coco.names
├── src/
│   ├── main.py
│   ├── detection/
│   │   └── detector.py
│   └── simulation/
│       └── drone_simulator.py
```

---
## **🔮 Future Improvements**

I’m always looking to make this project better! Some ideas for the future:
- Add custom-trained YOLOv8 weights for specific datasets
- Implement object tracking (e.g., DeepSORT or ByteTrack)
- Deploy as a web application for easy use

---
## **🤝 Who is this for?**
This project is perfect for:
- Students and researchers exploring computer vision
- Drone enthusiasts and hobbyists
- Anyone interested in real-time object detection

---
## **📬 Questions or Feedback?**
If you have any questions, suggestions, or just want to say hi, feel free to reach out! I’m always happy to connect with fellow developers and learners.

- Email: deekshithas369@gmail.com
- GitHub Issues: [Open an issue](https://github.com/YOUR_USERNAME/yolov8-target-tracker/issues)

---
## **📜 License**
This project is licensed under the [MIT License](LICENSE).