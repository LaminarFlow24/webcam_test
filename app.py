import cv2
import streamlit as st

# Title and instructions
st.title("Webcam Stream - Simple Alternative")
st.write("This app uses OpenCV to access the webcam and display the feed in Streamlit.")

# Start/Stop toggle
start_stream = st.checkbox("Start Webcam")

# Placeholder for the video feed
frame_placeholder = st.empty()

if start_stream:
    # Open the webcam
    cap = cv2.VideoCapture(0)

    # Check if webcam is accessible
    if not cap.isOpened():
        st.error("Unable to access the webcam. Please check permissions and retry.")
    else:
        st.info("Streaming webcam feed. Uncheck the box to stop.")
        while start_stream:
            ret, frame = cap.read()
            if not ret:
                st.error("Failed to read from webcam.")
                break

            # Convert BGR (OpenCV format) to RGB (Streamlit compatible)
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

            # Display the frame in Streamlit
            frame_placeholder.image(frame, channels="RGB")

            # Check if the checkbox is unchecked
            start_stream = st.session_state.get("start_webcam", False)

    # Release resources when the loop ends
    cap.release()
else:
    st.info("Check the 'Start Webcam' box to stream the video.")

