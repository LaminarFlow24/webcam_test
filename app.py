import cv2
import streamlit as st

st.title("Webcam Live Feed")
run = st.checkbox('Run')
FRAME_WINDOW = st.image([])
camera = cv2.VideoCapture(0)

if not camera.isOpened():
    st.error("Unable to access the webcam. Please check your camera settings.")

while run:
    ret, frame = camera.read()
    if ret:
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        FRAME_WINDOW.image(frame)
    else:
        st.error("Failed to capture frame from webcam. Please try again.")
else:
    st.write("Stopped")
    camera.release()  # Release the camera when stopping
