# Driver Drowsiness Detection System
This project combines two significant functionalities: detecting driver drowsiness using live video feed and enhancing images captured in low-light conditions. It uses computer vision techniques with OpenCV and dlib libraries to monitor a driver's alertness in real-time and applies image processing to improve the quality of low-light images.

## Features
- **Driver Drowsiness Detection:** Detects the state of the driver's eyes (open, closed, or drowsy) and classifies the driver's condition as "Sleeping", "Drowsy", or "Active". This functionality aims to enhance road safety by alerting if a driver shows signs of drowsiness.

- **Low Light Enhancement:** Enhances images taken in low-light conditions by adjusting brightness and contrast, applying bilateral filtering to reduce noise while preserving edges, and performing histogram equalization to enhance contrast.

## Dependencies
To run this project, you need the following libraries:

- OpenCV (cv2)
- NumPy
- dlib
- imutils

Ensure you have Python installed on your system. You can install these dependencies using pip:

```bash
pip install opencv-python numpy dlib imutils
```

## Setup

1. Clone the repository or download the project files.
2. Ensure you have the required dependencies installed.
3. Download the shape_predictor_68_face_landmarks.dat file from dlib's model repository and place it in the project directory for the drowsiness detection script to function.
   
## Running the Applications

### Driver Drowsiness Detection
To start the driver drowsiness detection, navigate to the project directory and run:

```bash
python driver_drowsiness.py
```

Make sure you have a webcam connected to your computer. Press ESC to exit the application.

### Low Light Image Enhancement
Place a low-light image with the filename lowLight.jpg in the project directory. Run the following command to enhance the image:

```bash
python lowLight.py
```

The enhanced image will be saved as improved_image.jpg in the project directory.
