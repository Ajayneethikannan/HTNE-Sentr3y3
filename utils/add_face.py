import face_recognition
import cv2
import numpy as np
import pickle
import os
import getpass
import sys



def add_face():
    video_capture = cv2.VideoCapture(0)

    while True:
        ret, frame = video_capture.read()
        cv2.imshow('Video', frame)
        # press c to capture photo
        if cv2.waitKey(1) & 0xFF == ord('c'):
            # make sure only person is in frame
            face_locations = face_recognition.face_locations(frame)
            try:
                face_encodings = face_recognition.face_encodings(
                frame, face_locations)[0]
            except:
                print("no face detected!")
            else:
                video_capture.release()
                cv2.destroyAllWindows()
                return face_encodings
