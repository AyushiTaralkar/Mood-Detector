import cv2
from deepface import DeepFace
import tensorflow as tf
import deepface

print(f"DeepFace version: {deepface.__version__}, TensorFlow version: {tf.__version__}")

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Could not open video device.")
    exit()

while True:
    ret, frame = cap.read()
    if not ret or frame is None:
        print("Error: Failed to capture frame.")
        break

    try:
        # DeepFace returns a list; get the first result's dominant emotion
        result = DeepFace.analyze(frame, actions=['emotion'], enforce_detection=False)
        # Usually result is a list of dicts, use the first detected face
        if isinstance(result, list) and len(result) > 0 and 'dominant_emotion' in result[0]:
            mood = result[0]['dominant_emotion']
            cv2.putText(frame, f"Mood: {mood}", (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        else:
            cv2.putText(frame, "No face detected", (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
    except Exception as e:
        cv2.putText(frame, "No face detected", (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
        print("Detection error:", e)

    cv2.imshow("Mood Detection", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        print("Exiting. User pressed 'q'.")
        break

cap.release()
cv2.destroyAllWindows()
