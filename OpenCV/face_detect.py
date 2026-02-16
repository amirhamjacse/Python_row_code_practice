# import cv2

# # Load the cascade file
# face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

# # Start webcam
# cap = cv2.VideoCapture(0)

# while True:
#     ret, frame = cap.read()
    
#     # Convert to grayscale
#     gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
#     # Detect faces
#     faces = face_cascade.detectMultiScale(
#         gray,
#         scaleFactor=1.3,
#         minNeighbors=5
#     )
    
#     # Draw rectangle around faces
#     for (x, y, w, h) in faces:
#         cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
    
#     cv2.imshow("Face Detection", frame)
    
#     # Press q to quit
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

# cap.release()
# cv2.destroyAllWindows()


from deepface import DeepFace
import cv2

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    try:
        result = DeepFace.analyze(
            frame,
            actions=['age', 'gender'],
            enforce_detection=False
        )

        age = result[0]['age']
        gender = result[0]['gender']

        text = f"Age: {age}, Gender: {gender}"
        cv2.putText(frame, text, (20, 40),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    1, (0, 255, 0), 2)

    except:
        pass

    cv2.imshow("Age Detection", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
