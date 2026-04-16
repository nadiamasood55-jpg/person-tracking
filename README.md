Real-Time Person Tracking System
Overview

This project is a real-time person detection and tracking system built using Python and OpenCV. It uses a webcam to detect a person and allows tracking of that person in real time.

Setup Instructions
Install Python (version 3.8 or higher recommended)
Install required library:
pip install opencv-python
(Optional) You can use any IDE. This project was developed using PhpStorm.
How to Run the Project
Open terminal in project folder
Run the script:
python your_script_name.py
Make sure your webcam is connected
Controls
Press s → Start tracking detected person
Press q → Quit the application
Approach

The system works in two main steps:

Person Detection
Uses HOG (Histogram of Oriented Gradients) with a pre-trained SVM model
Detects people in each frame using OpenCV
Person Tracking
When user presses s, the first detected person is selected
CSRT tracker is initialized to track that person
Tracker follows the person in real time
Tools Used
Python
OpenCV (cv2)
HOG + SVM (for detection)
CSRT Tracker (for tracking)
Webcam for video input
Features
Real-time person detection
Person tracking using CSRT
Bounding box around person
Displays coordinates (X, Y)
Simple keyboard controls
Limitations
Works best with one person
Detection may fail in low light
Not as accurate as deep learning models
Future Improvements
Add YOLO-based detection
Multi-person tracking
Improve accuracy and performance
License

This project is open-source and free to use.
uum-tpej-wxw
