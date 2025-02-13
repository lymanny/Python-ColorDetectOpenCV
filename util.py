import numpy as np  # NumPy for numerical operations
import cv2  # OpenCV for image processing


def get_limits(color):
    """
    Converts a BGR color to HSV and calculates the lower and upper HSV limits for color detection.
    This function is used to create a mask for detecting a specific color in an image or video.

    Parameters:
    color (list): A list containing BGR values of the target color.

    Returns:
    tuple: Lower and upper HSV limit arrays for color detection.
    """

    # Convert BGR color to HSV format
    c = np.uint8([[color]])  # Wrap color in a NumPy array
    hsvC = cv2.cvtColor(c, cv2.COLOR_BGR2HSV)  # Convert to HSV

    # Extract the Hue (H) component
    hue = hsvC[0][0][0]  # Get the hue value

    # Handle red hue wrap-around (since red is at both ends of the hue scale in OpenCV)
    if hue >= 165:  # Upper limit for red hue wrap-around
        lowerLimit = np.array([hue - 10, 100, 100], dtype=np.uint8)
        upperLimit = np.array([180, 255, 255], dtype=np.uint8)
    elif hue <= 15:  # Lower limit for red hue wrap-around
        lowerLimit = np.array([0, 100, 100], dtype=np.uint8)
        upperLimit = np.array([hue + 10, 255, 255], dtype=np.uint8)
    else:
        # For other colors, set standard HSV range with ±10 hue variation
        lowerLimit = np.array([hue - 10, 100, 100], dtype=np.uint8)
        upperLimit = np.array([hue + 10, 255, 255], dtype=np.uint8)

    return lowerLimit, upperLimit  # Return lower and upper HSV range
