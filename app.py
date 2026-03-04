import cv2

print("Face Detection System Started...")

# Load Haarcascade correctly
face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
)

# Start camera
cap = cv2.VideoCapture(0)

# Check camera
if not cap.isOpened():
    print("Error: Camera not opened")
    exit()
else:
    print("Camera started successfully")

while True:
    ret, frame = cap.read()
    if not ret:
        print("Failed to grab frame")
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.1, 5)

    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

    cv2.imshow("Face Detection", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        print("Application Closed Successfully")
        break

cap.release()
cv2.destroyAllWindows()