# Mood-Detector
This project detects your mood in real time using webcam video. It analyzes facial expressions with DeepFace and overlays the predicted emotion (happy, sad, angry, etc.) on the live video stream using Python and OpenCV. Press 'q' to exit anytime.

# Problem Definition
People need to understand emotions instantly in virtual meetings, online counseling, or interactive environments. Manual tracking is difficult—an automated solution can deliver real-time, objective mood insights using facial expressions from video.

# Requirement Analysis
Input: Live webcam feed (or video file) with clear faces.

Output: Detected mood/emotion label (happy, sad, angry, etc.), displayed on the live video stream.

Accuracy: Good detection with pre-trained DeepFace models (typically 70%+ on common emotions).

Speed: Real-time (1–5 fps) on consumer hardware.

Usability: Press 'q' to stop; mood appears overlaid on video window.

Top-Down Design / Modularization
Webcam Capture: Frame-by-frame video acquisition using OpenCV.

Face & Emotion Detection: Using DeepFace’s built-in emotion analysis model.

Result Overlay: Annotate each frame with detected mood label.

User Interface: Show live video with mood label, provide exit control.

# Algorithm/Implementation
Capture frame from webcam.

Run DeepFace.analyze (with enforce_detection=False) on each frame for emotion analysis.

Overlay dominant_emotion on the video using cv2.putText.

Display frames with OpenCV, update continually until user stops.

# Testing and Refinement
Verify on different faces, lighting, and backgrounds.

Check accuracy of detected emotions against actual expressions.

Ensure smooth frame rate and quick feedback.

Adjust camera position/lights if "No face detected" occurs too often.

# Tools/Libraries Used:

Python 3.x

OpenCV (opencv-python)

DeepFace

TensorFlow (tf-keras for DeepFace compatibility)
