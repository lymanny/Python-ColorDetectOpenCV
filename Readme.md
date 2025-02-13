# Python Color Detection using OpenCV

## Overview
This project is a **real-time color detection** application using **Python** and **OpenCV**. The script captures frames from a webcam, processes the image in the **HSV color space**, and detects a specified color by applying a color threshold.

## Features
- Real-time video processing from the webcam
- Detects a specific color in the video feed
- Draws a bounding box around the detected color
- Uses **HSV color space** for accurate color detection

## Installation
### Prerequisites
Ensure you have **Python 3.x** installed on your system.

### Install Required Libraries
Run the following command to install dependencies:
```sh
pip install -r requirements.txt
```

## Usage
1. Clone the repository:
   ```sh
   git clone https://github.com/2025-Testing/Python-ColorDetect-OpenCV.git
   cd Python-ColorDetect-OpenCV
   ```

2. Run the script:
   ```sh
   python main.py
   ```

3. Press **'q'** to exit the application.

## File Structure
```
Python-ColorDetect-OpenCV/
│── main.py                 # Main script for color detection
│── util.py                 # Helper functions (color range conversion)
│── requirements.txt        # Required dependencies
│── README.md               # Project documentation
```

## How It Works
1. **Captures a frame** from the webcam.
2. **Converts the frame** from BGR to HSV color space.
3. **Applies a threshold mask** to isolate the specified color.
4. **Finds the bounding box** around the detected area.
5. **Draws a rectangle** on the detected color region.
6. **Displays the live video feed** with real-time detection.

## Resources
This project was inspired by the tutorial: [Color Detection in OpenCV](https://www.youtube.com/watch?v=aFNDh5k3SjU).

## License
This project is licensed under the **MIT License** – see the [LICENSE](LICENSE.md) file for details.

