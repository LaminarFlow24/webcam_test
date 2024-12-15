import av
import streamlit as st
from streamlit_webrtc import webrtc_streamer, VideoTransformerBase

class VideoTransformer(VideoTransformerBase):
    def transform(self, frame):
        img = frame.to_ndarray(format="bgr24")  # Get the frame as a numpy array
        return av.VideoFrame.from_ndarray(img, format="bgr24")  # Return the same frame

st.title("Webcam Stream with Streamlit")
st.write("This app uses `streamlit-webrtc` to access your webcam and display the feed.")

# Stream webcam feed
webrtc_streamer(key="webcam", video_transformer_factory=VideoTransformer)
