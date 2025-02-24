import streamlit as st
import face_recognition
import cv2
import numpy as np
import csv
from datetime import datetime
import os
import time

# Initialize video capture
video_capture = None
face_detected = False

# Load known faces
Suliman_image = face_recognition.load_image_file("/home/suliman/Projects/Face_recognition_project/faces/suliman.jpg")
Suliman_encoding = face_recognition.face_encodings(Suliman_image)[0]
Umair_image = face_recognition.load_image_file("/home/suliman/Projects/Face_recognition_project/faces/umair.jpeg")
umair_encoding = face_recognition.face_encodings(Umair_image)[0]
Usman_image = face_recognition.load_image_file("/home/suliman/Projects/Face_recognition_project/faces/12.jpeg")
usman_encoding = face_recognition.face_encodings(Usman_image)[0]

known_face_encodings = [Suliman_encoding, umair_encoding, usman_encoding]
known_face_names = ['Suliman Roll number(034)', 'Umair(030)', 'Usman(020)']

# List of expected students
students = known_face_names.copy()

# Get the current time and date
now = datetime.now()
current_date = now.strftime("%Y-%m-%d")

# Create and open the CSV file
current_date = "2023-09-27"
csv_filename = f"{current_date}.csv"
f = open(csv_filename, "w+", newline="")
lnwriter = csv.writer(f)

# Streamlit UI
st.title("Face Recognition Attendance System")

start_detection = st.button("Start Face Detection")
stop_detection = st.empty()  # Placeholder for the stop button
stopped = False  # Flag to control loop termination

if start_detection:
    st.write("Face detection is running...")

    # Initialize video capture when the button is clicked
    video_capture = cv2.VideoCapture(0)
    face_detected = True

button_counter = 0

while face_detected and not stopped:
    _, frame = video_capture.read()
    small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
    rgb_small_frame = cv2.cvtColor(small_frame, cv2.COLOR_BGR2RGB)

    # Recognize faces
    face_locations = face_recognition.face_locations(rgb_small_frame)
    face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

    for face_encoding in face_encodings:
        matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
        face_distance = face_recognition.face_distance(known_face_encodings, face_encoding)
        best_match_index = np.argmin(face_distance)

        if matches[best_match_index]:
            name = known_face_names[best_match_index]

            # Add the text to the video
            if name in known_face_names:
                font = cv2.FONT_HERSHEY_SIMPLEX
                bottomLeftCornerOfText = (10, 100)
                fontScale = 1.5
                fontColor = (0, 255, 0)
                thickness = 3
                lineType = 2
                cv2.putText(frame, name + " Present", bottomLeftCornerOfText, font, fontScale, fontColor, thickness, lineType)

                if name in students:
                    students.remove(name)
                    current_time = now.strftime("%H-%M-%S")
                    lnwriter.writerow([name, current_time])

                    # Delay before announcing the presence of the recognized person
                    time.sleep(1)

                    # Use espeak to announce the presence of the recognized person
                    os.system(f"espeak '{name} is present'")

    # Display the video frame in Streamlit
    st.image(frame, channels="BGR", use_column_width=True)

    # Check if the stop button is clicked
    if stop_detection.button("Stop Face Detection"):
        stopped = True

# Release resources and close the CSV file
if video_capture:
    video_capture.release()
f.close()
