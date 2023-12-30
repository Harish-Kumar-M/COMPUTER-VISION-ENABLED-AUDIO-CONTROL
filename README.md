# COMPUTER-VISION-ENABLED-AUDIO-CONTROL
Implemented a Python script leveraging OpenCV for real-time hand gesture recognition. The script captures video from a webcam, detects the user's hand within a defined Region of Interest (ROI), and dynamically adjusts the system volume based on the hand's position. This hands-free volume control mechanism enhances user accessibility and showcases proficiency in computer vision and automation using Python.

Overview
This Python script utilizes OpenCV for real-time hand gesture recognition, enabling hands-free control of system volume. The script captures video from a webcam, detects the user's hand within a predefined Region of Interest (ROI), and dynamically adjusts the system volume based on the hand's position.

# Features
Real-time hand gesture recognition.
Hands-free system volume adjustment.
User-friendly interface leveraging computer vision.
# Requirements
Python 3.x
OpenCV (pip install opencv-python)
NumPy (pip install numpy)
PyAutoGUI (pip install pyautogui)
# Usage
Install the required dependencies using pip install -r requirements.txt.
Run the script: python hand_gesture_volume_control.py.
Position your hand within the ROI displayed on the webcam feed.
Adjust the system volume by moving your hand.
Configuration
Modify the ROI coordinates in the script for a different hand detection area.
Tweak the HSV color range for optimal skin color detection.
# Notes
Ensure proper lighting conditions for accurate hand detection.
Press 'q' to exit the script.
Contributing
Feel free to contribute by forking the repository and creating a pull request. Bug reports and feature requests are welcome.

License
This project is licensed under the MIT License.
