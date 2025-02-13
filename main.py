import cv2  # OpenCV for image processing
from PIL import Image  # PIL for bounding box detection
from util import get_limits  # Import the function to get HSV color limits

# Define the color to detect (Green in BGR colorspace)
green = [0, 255, 0]  # Note: This is actually GREEN in BGR

# Open the webcam (0 = default camera, 1/2 = external cameras if available)
cap = cv2.VideoCapture(0)

# Check if the camera opened successfully
if not cap.isOpened():
    print("Error: Could not access the camera.")
    exit()

# Process video frames in a continuous loop
while True:
    # Capture a frame from the webcam
    ret, frame = cap.read()

    # If the frame was not captured correctly, break the loop
    if not ret:
        print("Error: Could not read frame.")
        break

    # Convert the captured frame from BGR to HSV color space for better color segmentation
    hsvImage = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Get the lower and upper HSV color limits for the selected color
    lowerLimit, upperLimit = get_limits(color=green)

    # Create a binary mask where detected color pixels are white (255) and the rest are black (0)
    mask = cv2.inRange(hsvImage, lowerLimit, upperLimit)

    # Convert the mask to a PIL image to detect the bounding box
    mask_ = Image.fromarray(mask)

    # Get the bounding box coordinates of the detected color area
    bbox = mask_.getbbox()

    # If a bounding box is found, draw a rectangle around the detected area
    if bbox is not None:
        x1, y1, x2, y2 = bbox  # Extract bounding box coordinates
        frame = cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 5)  # Draw a green rectangle

    # Display the frame with the bounding box
    cv2.imshow('frame', frame)

    # Exit the loop if the 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the webcam resource and close all OpenCV windows
cap.release()
cv2.destroyAllWindows()
