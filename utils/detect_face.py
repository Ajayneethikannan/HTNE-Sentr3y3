import time, cv2, pickle, os, face_recognition

def detect_face():

    video_capture = cv2.VideoCapture(0)
    userData = os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..', 'userData'))
    with open( f"{userData}/faces_encodings.txt", "rb") as fp:
        known_face_encodings = pickle.load(fp)

    with open(f"{userData}/ids.txt", "rb") as fp:
        known_face_ids = pickle.load(fp)

    count = 0 # take 10 snapshots, at intervals of 0.1 seconds

    while count < 10:
        ret, frame = video_capture.read()
        small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
        rgb_small_frame = small_frame[:, :, ::-1]
        face_locations = face_recognition.face_locations(
                rgb_small_frame)
        face_encodings = face_recognition.face_encodings(
                rgb_small_frame, face_locations)
        for face_encoding in face_encodings:
            matches = face_recognition.compare_faces(
                known_face_encodings, face_encoding)
                
            if True in matches:
                face_indices = [i for i, val in enumerate(matches) if val] 
                id = [known_face_ids[i] for i in face_indices]

                # If found then exit
                video_capture.release()
                cv2.destroyAllWindows()
                return (id[0], 0.1*count) # Since we are attempting 10 times, we need to add the seconds accurately depending on number of attempts
                    
            else:
                video_capture.release()
                cv2.destroyAllWindows()
                return (-1, 0.1*count) # Since we are attempting 10 times, we need to add the seconds accurately depending on number of attempts
        
        count = count + 1
        time.sleep(0.1)

    print('video timeout has been reached')
    video_capture.release()
    cv2.destroyAllWindows()
    return None, 1 # Return non if no one is using the computer










