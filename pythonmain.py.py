import numpy as np
import math
import cv2
import pyautogui

# Initialize variables
cap = cv2.VideoCapture(0)
prev_vol = 0

while True:
    # Read a frame from the webcam
    ret, frame = cap.read()

    # Flip the frame horizontally
    frame = cv2.flip(frame, 1)

    # Region of Interest (ROI) for detecting the hand
    roi = frame[100:300, 100:300]

    # Draw a rectangle around the ROI
    cv2.rectangle(frame, (100, 100), (300, 300), (0, 255, 0), 0)

    # Convert the ROI to HSV
    hsv = cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)

    # Define a range for skin color in HSV
    lower_skin = np.array([0, 20, 70], dtype=np.uint8)
    upper_skin = np.array([20, 255, 255], dtype=np.uint8)

    # Create a binary mask for the skin color
    mask = cv2.inRange(hsv, lower_skin, upper_skin)

    # Find contours in the binary image
    contours, _ = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Find the contour with the maximum area (the hand)
    if len(contours) > 0:
        hand_contour = max(contours, key=lambda x: cv2.contourArea(x))

        # Calculate the centroid of the hand
        M = cv2.moments(hand_contour)
        if M["m00"] != 0:
            cx = int(M["m10"] / M["m00"])
            cy = int(M["m01"] / M["m00"])
            cv2.circle(roi, (cx, cy), 5, [0, 0, 255], -1)

            # Calculate the distance from the centroid to the center of the ROI
            distance = math.sqrt((cx - 150) ** 2 + (cy - 150) ** 2)

            # Map the distance to a volume range (0 to 100)
            volume = int(np.interp(distance, [0, 100], [0, 100]))

            # Adjust the volume if it has changed
            if volume != prev_vol:
                pyautogui.press("volumeup" if volume > prev_vol else "volumedown")
                prev_vol = volume

    # Display the frame
    cv2.imshow("Hand Gesture Volume Control", frame)

    # Check for the 'q' key to exit the loop
    key = cv2.waitKey(1)
    if key == ord("q"):
        break

# Release the camera and close OpenCV windows
cap.release()
cv2.destroyAllWindows()
cv2.waitKey(1)  # Ensure all OpenCV windows are closed
cv2.waitKey(1)  # Additional wait
cv2.waitKey(1)  # Additional wait
cv2.waitKey(1)  # Additional wait
