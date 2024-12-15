import cv2
import streamlit as st
import numpy as np

st.title("Webcam Stream with OpenCV")
st.write("This app uses OpenCV to access your webcam and display the feed in Streamlit.")

# Placeholder for the video stream
frame_placeholder = st.empty()

# Start/Stop button for the webcam
run_webcam = st.button("Start/Stop Webcam")

# Webcam loop
if "webcam_running" not in st.session_state:
    st.session_state.webcam_running = False

if run_webcam:
    st.session_state.webcam_running = not st.session_state.webcam_running

if st.session_state.webcam_running:
    # Open the webcam
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        st.error("Unable to access the webcam. Check your permissions.")
    else:
        st.info("Press the 'Start/Stop Webcam' button to stop streaming.")
        while st.session_state.webcam_running:
            ret, frame = cap.read()
            if not ret:
                st.error("Failed to capture video.")
                break

            # Convert BGR (OpenCV format) to RGB (Streamlit compatible)
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

            # Display the frame in Streamlit
            frame_placeholder.image(frame, channels="RGB")

            # Stop streaming if the button is pressed again
            if not st.session_state.webcam_running:
                break

    cap.release()
    cv2.destroyAllWindows()
else:
    st.info("Click the 'Start/Stop Webcam' button to start streaming.")
