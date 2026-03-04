# Real-Time Face Detection System 👤

This project is a Real-Time Face Detection System built using Python and OpenCV.  
It detects human faces from live webcam video using Haar Cascade Classifier.

---

## 📌 Project Description

The system captures live video from the webcam and detects faces in real-time.  
It draws a rectangle around detected faces using OpenCV's built-in Haar Cascade model.

This project demonstrates basic computer vision concepts and real-time object detection.

---

##  Technologies Used

- Python
- OpenCV
- Haar Cascade Classifier

---

##  Project Structure

Face-Detection-OpenCV/
│
├── app.py
├── haarcascade_frontalface_default.xml
└── README.md

---

## ⚙️ How It Works

1. Access webcam using OpenCV.
2. Convert each frame to grayscale.
3. Apply Haar Cascade classifier.
4. Detect faces using detectMultiScale().
5. Draw rectangle around detected faces.
6. Display real-time output window.

---

## How to Run the Project

1. Install Python (3.x)
2. Install OpenCV:

```bash
pip install opencv-python
