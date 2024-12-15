import streamlit as st
from streamlit_webrtc import webrtc_streamer
import av
from streamlit_webrtc import VideoTransformerBase

# Title and description
st.title("Webcam Stream with Streamlit")
st.write("This app uses `streamlit-webrtc` to access your webcam and display the feed.")

# VideoTransformer class to process video frames
class VideoTransformer(VideoTransformerBase):
    def transform(self, frame):
        img = frame.to_ndarray(format="bgr24")  # Get the frame as a numpy array
        return av.VideoFrame.from_ndarray(img, format="bgr24")  # Return the frame as it is

# Stream webcam feed
webrtc_streamer(
    key="webcam",
    video_transformer_factory=VideoTransformer,
    rtc_configuration={"iceServers": [{"urls": ["stun:stun.l.google.com:19302"]}]}
)
